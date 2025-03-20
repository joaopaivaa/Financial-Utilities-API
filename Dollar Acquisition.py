import requests
import json
import pandas as pd
from datetime import datetime

# Acquisition ################################################################################################

def get_us_inflation_rate(start_year, end_year):

    # Bureau of Labor Statistics API URL
    url = "https://api.bls.gov/publicAPI/v2/timeseries/data/"

    # CPI-U (All Items) - Seasonaly Adjusted
    series_id = ["CUSR0000SA0"]

    headers = {"Content-Type": "application/json"}
    data = {
        "seriesid": series_id,
        "startyear": start_year,
        "endyear": end_year,
        "registrationkey": "66a24c4f75bb424692f67dedcfb3e6cb"  # Se não tiver, pode remover esta linha
    }

    response = requests.post(url, headers=headers, data=json.dumps(data))

    if response.status_code == 200:
        result = response.json()
        
        dados = result["Results"]["series"][0]["data"]
        
    else:
        print("Request error: ", response.status_code)

    return dados

df_1 = get_us_inflation_rate('1966', '1986')
df_2 = get_us_inflation_rate('1986', '2006')
df_3 = get_us_inflation_rate('2006', '2026')

df = pd.DataFrame(df_1 + df_2 + df_3)
df = df.sort_values(by=['year', 'period']).reset_index(drop=True)

df["year"] = df["year"].astype(int)
df["CPI Value"] = df["value"].astype(float)
df["month"] = df["period"].str.extract("(\d+)").astype(int)
df["Date"] = pd.to_datetime(df[["year", "month"]].assign(day=1))

df = df.sort_values("Date")

df["Monthly Inflation"] = ((df["CPI Value"] / df["CPI Value"].shift(1)) - 1) * 100

df = df.dropna(subset='Monthly Inflation')
df = df[["Date", "CPI Value", "Monthly Inflation"]]

# Cleaning ################################################################################################

df['Monthly Inflation'] = pd.to_numeric(df['Monthly Inflation']) / 100
df['Month Number'] = [int(datetime.strftime(df['Date'][index], format='%m')) for index in df.index]

df = df[df['Date'] >= pd.to_datetime('01/01/1967', format='%d/%m/%Y')].reset_index(drop=True)

df_days_per_month = pd.read_csv("C:\\Users\\e-joaom\\Downloads\\months_days.csv")

df = df.merge(df_days_per_month, on='Month Number', how='left')

df[(df['Month'] == 'February') &
   (df['Date'].dt.year.astype(int) % 4 == 0) &
   ((df['Date'].dt.year.astype(int) % 100 != 0) | (df['Date'].dt.year.astype(int) % 400 == 0))]['Number of Days'] = 29

df_daily_inflation = pd.DataFrame(columns=['Date', 'Daily Inflation'])
for i in df.index:
    df_date = pd.DataFrame(columns=['Date', 'Daily Inflation'])
    df_date['Date'] = pd.date_range(start=df['Date'].values[i], periods=df['Number of Days'].values[i])
    df_date['Daily Inflation'] = ((1 + df['Monthly Inflation'].values[i])**(1/df['Number of Days'].values[i])) - 1
    df_daily_inflation = pd.concat([df_daily_inflation, df_date], ignore_index=True)

df_daily_inflation.to_csv('Dollar Daily Inflation.csv', index=False)
