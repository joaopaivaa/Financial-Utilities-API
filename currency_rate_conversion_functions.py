import pandas as pd
from typing import List

def currency_rate_conversion(dates: List[str], values: List[float], original_currency: str):

    df_currencies = pd.read_csv('Currencies Rate.csv')

    df = pd.DataFrame({'Date': dates, original_currency: values})
    
    if original_currency is 'GBP':
        df = df.merge(df_currencies, on='Date', how='left')
        df['USD'] = df[original_currency] * df['GBP-USD']
        df['EUR'] = df[original_currency] * df['GBP-EUR']

    elif original_currency is 'EUR':
        df = df.merge(df_currencies, on='Date', how='left')
        df['USD'] = df[original_currency] * df['EUR-USD']
        df['GBP'] = df[original_currency] * df['EUR-GBP']

    elif original_currency is 'USD':
        df = df.merge(df_currencies, on='Date', how='left')
        df['GBP'] = df[original_currency] * df['USD-GBP']
        df['EUR'] = df[original_currency] * df['USD-EUR']

    else:
        return 'Please, select a currency between EUR, USD and GBP'
    
    df = df.drop(columns=['EUR-USD', 'EUR-GBP', 'GBP-USD', 'GBP-EUR', 'USD-GBP', 'USD-EUR'])
    
    return df
