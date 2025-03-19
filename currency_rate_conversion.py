import pandas as pd
from typing import List

def rate_conversion(dates: List[str], values: List[float], original_currency: str):

    df = pd.DataFrame({'Date': dates, original_currency: values})
    
    if original_currency is 'Great Britain Pound':
        df = df.merge(df_currencies, on='Date', how='left')
        df['Dollar'] = df[original_currency] * df['GBP-USD']
        df['Euro'] = df[original_currency] * df['GBP-EUR']

    elif original_currency is 'Euro':
        df = df.merge(df_currencies, on='Date', how='left')
        df['Dollar'] = df[original_currency] * df['EUR-USD']
        df['Great Britain Pound'] = df[original_currency] * df['EUR-GBP']

    elif original_currency is 'Dollar':
        df = df.merge(df_currencies, on='Date', how='left')
        df['Great Britain pound'] = df[original_currency] * df['USD-GBP']
        df['Euro'] = df[original_currency] * df['USD-EUR']

    else:
        return 'Please, select a currency between Euro, Dollar and Great Britain Pound'
    
    df = df.drop(columns=['EUR-USD', 'EUR-GBP', 'GBP-USD', 'GBP-EUR', 'USD-GBP', 'USD-EUR'])
    
    return df
