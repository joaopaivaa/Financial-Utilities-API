import requests
import pandas as pd
from datetime import datetime

url = "https://api.bcb.gov.br/dados/serie/bcdata.sgs.433/dados?formato=json"
response = requests.get(url)
data = response.json()

df_ipca = pd.DataFrame(data)
df_ipca.rename(columns={'data': 'Date', 'valor': 'IPCA Value'}, inplace=True)
df_ipca['Date'] = pd.to_datetime(df_ipca['Date'], format='%d/%m/%Y')
df_ipca['IPCA Value'] = pd.to_numeric(df_ipca['IPCA Value']) / 100
df_ipca['Month Number'] = [int(datetime.strftime(df_ipca['Date'][index], format='%m')) for index in df_ipca.index]

df_ipca = df_ipca[df_ipca['Date'] >= pd.to_datetime('01/07/1994', format='%d/%m/%Y')].reset_index(drop=True)

df_days_per_month = pd.read_csv("months_days.csv")

df_ipca = df_ipca.merge(df_days_per_month, on='Month Number', how='left')

df_ipca[(df_ipca['Month'] == 'February') &
        (df_ipca['Date'].dt.year.astype(int) % 4 == 0) &
        ((df_ipca['Date'].dt.year.astype(int) % 100 != 0) | (df_ipca['Date'].dt.year.astype(int) % 400 == 0))]['Number of Days'] = 29

df_daily_ipca = pd.DataFrame(columns=['Date', 'IPCA Value'])
for i in df_ipca.index:
    df_date = pd.DataFrame(columns=['Date', 'IPCA Value'])
    df_date['Date'] = pd.date_range(start=df_ipca['Date'].values[i], periods=df_ipca['Number of Days'].values[i])
    df_date['IPCA Value'] = ((1 + df_ipca['IPCA Value'].values[i])**(1/df_ipca['Number of Days'].values[i])) - 1
    df_daily_ipca = pd.concat([df_daily_ipca, df_date], ignore_index=True)

df_daily_ipca.to_csv('BRL Daily Inflation.csv', index=False)
