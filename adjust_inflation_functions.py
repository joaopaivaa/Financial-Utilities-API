import pandas as pd

def adjust_BRL_inflation(dates:str, values:float, present_date:str=df_daily_ipca['Date'].max()):

    df_daily_ipca = pd.read_csv('BRL Daily Inflation.csv')

    df = pd.DataFrame(columns=['Date', 'Value'])
    df['Date'] = dates
    df['Date'] = pd.to_datetime(df['Date'], format='%d/%m/%Y')
    df['Value'] = values

    present_date = pd.to_datetime(present_date, format='%d/%m/%Y')
    df_daily_ipca_to_present_date = df_daily_ipca[df_daily_ipca['Date'] <= present_date]
    df_daily_ipca_to_present_date['IPCA Value Accumulated'] = (1 + df_daily_ipca_to_present_date['IPCA Value'])[::-1].cumprod()[::-1] - 1

    if present_date <= df_daily_ipca_to_present_date['Date'].max():
        df = df[(df['Date'] >= df_daily_ipca_to_present_date['Date'].min()) & (df['Date'] < present_date)]
    else:
        return f'The present date must be less than or equal to {df_daily_ipca_to_present_date['Date'].max().date()}'

    df = df.merge(df_daily_ipca_to_present_date, on='Date', how='left')
    df[f'Adjusted Value - {present_date}'] = df['Value'] * (1 + df['IPCA Value Accumulated'])

    return df
