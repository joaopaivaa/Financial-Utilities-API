import requests
import json
import pandas as pd
from datetime import datetime
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Acquisition ################################################################################################

def get_us_inflation_rate(start_year, end_year):

    # CPI-U (All Items) - Seasonaly Adjusted
    series_id = ["CUUR0000SA0"]

    headers = {"Content-Type": "application/json"}
    data = {
        "seriesid": series_id,
        "startyear": start_year,
        "endyear": end_year,
        "registrationkey": "66a24c4f75bb424692f67dedcfb3e6cb"
    }

    # Bureau of Labor Statistics API URL
    url = "https://api.bls.gov/publicAPI/v2/timeseries/data/"
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

if '-' in df['value'].values:

    indexes = df[df["value"] == '-'].index
    for index in indexes:
        
        previous_value = float(df.at[index - 1, 'value'])
        next_value = float(df.at[index + 1, 'value'])
        df.at[index, 'value'] = str(previous_value)

df["CPI Value"] = df["value"].astype(float)
df["month"] = df["period"].str.extract("(\d+)").astype(int)
df["Date"] = pd.to_datetime(df[["year", "month"]].assign(day=1))

df = df.sort_values("Date")

df = df[["Date", "CPI Value"]]

# Cleaning ################################################################################################

df['Month Number'] = [int(datetime.strftime(df['Date'][index], format='%m')) for index in df.index]
df['Year Number'] = [int(datetime.strftime(df['Date'][index], format='%Y')) for index in df.index]

df = df[df['Date'] >= pd.to_datetime('01/01/1967', format='%d/%m/%Y')].reset_index(drop=True)

df.to_csv(BASE_DIR + '\databases\\USD Monthly Inflation.csv', index=False, encoding='utf-8')