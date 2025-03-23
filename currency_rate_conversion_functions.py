import pandas as pd
from typing import List
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def currency_rate_conversion(dates: List[str], values: List[float], original_currency: str):

    df_currencies = pd.read_csv(BASE_DIR + '/databases/Currencies Rate.csv', sep=';')
    df_currencies['Date'] = pd.to_datetime(df_currencies['Date'])

    df = pd.DataFrame({'Date': dates, original_currency: values})
    df['Date'] = pd.to_datetime(df['Date'])

    df = df.merge(df_currencies, on='Date', how='left')
    for i in df.index:
        if (i > 0) and all(pd.isna([df.iloc[i, column_n] for column_n in range(2,9)])) and (not any(pd.isna([df.iloc[i-1, column_n] for column_n in range(2,9)]))):
            for column_n in range(2,9):
                df.iloc[i, column_n] = df.iloc[i-1, column_n]
    
    if original_currency == 'GBP':
        df['USD'] = df[original_currency].astype(float) * df['GBPUSD=X'].astype(float)
        df['EUR'] = df[original_currency].astype(float) * df['GBPEUR=X'].astype(float)

    elif original_currency == 'EUR':
        df['USD'] = df[original_currency].astype(float) * df['EURUSD=X'].astype(float)
        df['GBP'] = df[original_currency].astype(float) * df['EURGBP=X'].astype(float)

    elif original_currency == 'USD':
        df['GBP'] = df[original_currency].astype(float) * df['GBP=X'].astype(float)
        df['EUR'] = df[original_currency].astype(float) * df['EUR=X'].astype(float)

    else:
        return 'Please, select a currency between EUR, USD and GBP'
    
    df = df.drop(columns=['EURUSD=X', 'EURGBP=X', 'GBPUSD=X', 'GBPEUR=X', 'GBP=X', 'EUR=X'])
    
    return df
