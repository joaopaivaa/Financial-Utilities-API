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

    months_filter = 'JAN|FEB|MAR|APR|MAY|JUN|JUL|AUG|SEP|OCT|NOV|DEC'

    df.columns = ['Date', 'Monthly Inflation']
    df = df[df['Date'].str.contains(months_filter, case=True, na=False)].reset_index(drop=True)

    df['Date'] = pd.to_datetime(df['Date'], format="%Y %b")
    df['Month Number'] = [int(datetime.strftime(df['Date'][index], format='%m')) for index in df.index]
    df['Year Number'] = [int(datetime.strftime(df['Date'][index], format='%Y')) for index in df.index]

    df['Monthly Inflation'] = pd.to_numeric(df['Monthly Inflation']) / 100

    df.to_csv(BASE_DIR + '\databases\GBP Monthly Inflation.csv', index=False, encoding='utf-8')

else:
    print("Request error: ", response.status_code)