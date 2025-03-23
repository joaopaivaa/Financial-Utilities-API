import requests
import pandas as pd
from datetime import datetime
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

url = "https://api.bcb.gov.br/dados/serie/bcdata.sgs.433/dados?formato=json"
response = requests.get(url)
data = response.json()

df = pd.DataFrame(data)
df.rename(columns={'data': 'Date', 'valor': 'Monthly Inflation'}, inplace=True)
df['Date'] = pd.to_datetime(df['Date'], format='%d/%m/%Y')
df['Monthly Inflation'] = pd.to_numeric(df['Monthly Inflation']) / 100
df['Month Number'] = [int(datetime.strftime(df['Date'][index], format='%m')) for index in df.index]

df = df[df['Date'] >= pd.to_datetime('01/07/1994', format='%d/%m/%Y')].reset_index(drop=True)

df_days_per_month = pd.read_csv(BASE_DIR + "\databases\months_days.csv")

df = df.merge(df_days_per_month, on='Month Number', how='left')

df.loc[
    (df['Month'] == 'February') &
    (df['Date'].dt.year % 4 == 0) &
    ((df['Date'].dt.year % 100 != 0) | (df['Date'].dt.year % 400 == 0)),
    'Number of Days'
] = 29

df_daily_ipca = pd.DataFrame(columns=['Date', 'Daily Inflation'])
for i in df.index:
    df_date = pd.DataFrame(columns=['Date', 'Daily Inflation'])
    df_date['Date'] = pd.date_range(start=df['Date'].values[i], periods=df['Number of Days'].values[i])
    df_date['Daily Inflation'] = ((1 + df['Monthly Inflation'].values[i])**(1/df['Number of Days'].values[i])) - 1
    df_daily_ipca = pd.concat([df_daily_ipca, df_date], ignore_index=True)

df_daily_ipca.to_csv(BASE_DIR + '\databases\BRL Daily Inflation.csv', index=False)
