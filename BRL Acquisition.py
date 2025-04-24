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
df['Year Number'] = [int(datetime.strftime(df['Date'][index], format='%Y')) for index in df.index]

df = df[df['Date'] >= pd.to_datetime('01/07/1994', format='%d/%m/%Y')].reset_index(drop=True)

df.to_csv(BASE_DIR + '\databases\BRL Monthly Inflation.csv', index=False)