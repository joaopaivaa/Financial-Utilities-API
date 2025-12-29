import pandas as pd
from typing import Literal
import os
from datetime import datetime

def inflation_adjustment(dates:list[str], values:list[float], currency:Literal['BRL','GBP','USD'], present_date:str=None):

    BASE_DIR = os.path.dirname(os.path.abspath(__file__))

    if currency == 'BRL':
        df_monthly_ipca = pd.read_csv(rf'{BASE_DIR}/databases/BRL Monthly Inflation.csv')

    elif currency == 'USD':
        df_monthly_ipca = pd.read_csv(rf'{BASE_DIR}/databases/USD Monthly Inflation.csv')

    elif currency == 'GBP':
        df_monthly_ipca = pd.read_csv(rf'{BASE_DIR}/databases/GBP Monthly Inflation.csv')

    else:
        return "Currency not supported. Please select 'BRL', 'GBP', or 'USD'."

    df_monthly_ipca['Date'] = pd.to_datetime(df_monthly_ipca['Date'])

    present_date = df_monthly_ipca['Date'].max() if present_date == None else present_date

    df = pd.DataFrame({'Date': dates, 
                       'Value': values})
    
    df['Date'] = pd.to_datetime(df['Date'])
    df['Month Number'] = [int(datetime.strftime(df['Date'][index], format='%m')) for index in df.index]
    df['Year Number'] = [int(datetime.strftime(df['Date'][index], format='%Y')) for index in df.index]

    present_date = pd.to_datetime(present_date)
    df_monthly_ipca_to_present_date = df_monthly_ipca[df_monthly_ipca['Date'] <= present_date].copy()
    df_monthly_ipca_to_present_date['Accumulated Inflation'] = (1 + df_monthly_ipca_to_present_date['Monthly Inflation'])[::-1].cumprod()[::-1] - 1

    if present_date <= df_monthly_ipca_to_present_date['Date'].max() + pd.DateOffset(months=1):
        df = df[(df['Date'] >= df_monthly_ipca_to_present_date['Date'].min()) & (df['Date'] <= present_date)]
    else:
        return f"The present date must be less than or equal to {df_monthly_ipca_to_present_date['Date'].max().date()}"

    df = df.merge(df_monthly_ipca_to_present_date, on=['Month Number','Year Number'], how='left')
    df.columns = df.columns.str.replace('Date_x', 'Date', regex=False)
    df[f'Adjusted Value - {present_date.month}/{present_date.year}'] = round(df['Value'] * (1 + df['Accumulated Inflation']), 2)

    df['Accumulated Inflation (%)'] = round(df['Accumulated Inflation'] * 100, 2)
    df = df.drop(columns=['Monthly Inflation', 'Month Number', 'Year Number', 'Accumulated Inflation', 'Date_y'], axis=1)

    return df