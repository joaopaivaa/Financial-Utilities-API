import requests
import pandas as pd
from datetime import datetime
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

url = "https://apisidra.ibge.gov.br/values/t/1737/n1/all/v/2266/p/all/d/v2266%2013"
response = requests.get(url)

if response.status_code == 200:

    data = response.json()
    df = pd.DataFrame(data)

    df = df[['D3C', 'V']]
    df.rename(columns={'D3C': 'Date', 'V': 'CPI Value'}, inplace=True)

    df = df[1:].reset_index(drop=True)

    df['Date'] = pd.to_datetime(df['Date'] + '01')
    df['Month Number'] = [int(datetime.strftime(df['Date'][index], format='%m')) for index in df.index]
    df['Year Number'] = [int(datetime.strftime(df['Date'][index], format='%Y')) for index in df.index]

    df = df[df['Date'] >= pd.to_datetime('01/07/1994', format='%d/%m/%Y')].reset_index(drop=True)

    df['CPI Value'] = df['CPI Value'].astype(float).round(2)

    df.to_csv(BASE_DIR + '\databases\BRL Monthly Inflation.csv', index=False)

else:
    print("Request error: ", response.status_code)