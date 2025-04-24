import pandas as pd
import os
from datetime import datetime

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

df = pd.read_csv(BASE_DIR + '\databases\GBP Monthly Inflation.csv', sep=';')

df['Date'] = pd.to_datetime(df['Date'], format='%d/%m/%Y')
df['Month Number'] = [int(datetime.strftime(df['Date'][index], format='%m')) for index in df.index]
df['Year Number'] = [int(datetime.strftime(df['Date'][index], format='%Y')) for index in df.index]

df.drop(columns=['Monthly Inflation (%)'], inplace=True)

df.to_csv(BASE_DIR + '\databases\GBP Monthly Inflation.csv', index=False, encoding='utf-8')