import pandas as pd
import os
from datetime import datetime

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

df = pd.read_csv(BASE_DIR + '\databases\GBP Monthly Inflation.csv', sep=';')

df['Date'] = pd.to_datetime(df['Date'], format='%d/%m/%Y')
df['Month Number'] = [int(datetime.strftime(df['Date'][index], format='%m')) for index in df.index]

df_days_per_month = pd.read_csv(BASE_DIR + "\databases\months_days.csv")

df = df.merge(df_days_per_month, on='Month Number', how='left')

df.loc[
    (df['Month'] == 'February') &
    (df['Date'].dt.year % 4 == 0) &
    ((df['Date'].dt.year % 100 != 0) | (df['Date'].dt.year % 400 == 0)),
    'Number of Days'
] = 29

df_daily_inflation = pd.DataFrame(columns=['Date', 'Daily Inflation'])
for i in df.index:
    df_date = pd.DataFrame(columns=['Date', 'Daily Inflation'])
    df_date['Date'] = pd.date_range(start=df['Date'].values[i], periods=df['Number of Days'].values[i])
    df_date['Daily Inflation'] = ((1 + df['Monthly Inflation'].values[i])**(1/df['Number of Days'].values[i])) - 1
    df_daily_inflation = pd.concat([df_daily_inflation, df_date], ignore_index=True)

df_daily_inflation.to_csv(BASE_DIR + '\databases\GBP Daily Inflation.csv', index=False, encoding='utf-8')
