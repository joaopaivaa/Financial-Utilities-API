import pandas as pd
import os
from datetime import datetime
import requests
from io import StringIO

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

url = "https://www.ons.gov.uk/generator?format=csv&uri=/economy/inflationandpriceindices/timeseries/d7g7/mm23"
response = requests.get(url)

if response.status_code == 200:

    df = pd.read_csv(StringIO(response.text))

    df = df.loc[189:,]
    df.columns = ['Date', 'Monthly Inflation']

    df['Date'] = pd.to_datetime(df['Date'], format="%Y %b")
    df['Month Number'] = [int(datetime.strftime(df['Date'][index], format='%m')) for index in df.index]
    df['Year Number'] = [int(datetime.strftime(df['Date'][index], format='%Y')) for index in df.index]

    df['Monthly Inflation'] = pd.to_numeric(df['Monthly Inflation']) / 100

    df.to_csv(BASE_DIR + '\databases\GBP Monthly Inflation.csv', index=False, encoding='utf-8')

else:
    print("Request error: ", response.status_code)