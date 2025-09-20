import yfinance as yf
import pandas as pd
import os
from datetime import datetime

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

previous_df = pd.read_csv(os.path.join(BASE_DIR, 'databases\Currencies Rate.csv'), sep=';')

previous_date = previous_df.iloc[-1]['Date']
actual_date = str(pd.to_datetime(datetime.now()).date())

if not (actual_date in previous_df['Date'].values):

    eur_usd = yf.download(['EURUSD=X'], start=previous_date, end=actual_date)[['Close']]

    eur_gbp = yf.download(['EURGBP=X'], start=previous_date, end=actual_date)[['Close']]

    gbp_usd = yf.download(['GBPUSD=X'], start=previous_date, end=actual_date)[['Close']]

    gbp_eur = yf.download(['GBPEUR=X'], start=previous_date, end=actual_date)[['Close']]

    usd_gbp = yf.download(['GBP=X'], start=previous_date, end=actual_date)[['Close']]

    usd_eur = yf.download(['EUR=X'], start=previous_date, end=actual_date)[['Close']]

    df_currencies = pd.concat([eur_usd, eur_gbp, gbp_usd, gbp_eur, usd_gbp, usd_eur], axis=1, join="outer")['Close']
    df_currencies = df_currencies.reset_index().rename(columns={'index': 'Date'})
    df_currencies['Date'] = df_currencies['Date'].astype(str)

    df_currencies = pd.concat([previous_df, df_currencies], ignore_index=True)
    df_currencies = df_currencies.drop_duplicates('Date').reset_index(drop=True)

    dates_list = pd.date_range(start=previous_df['Date'].min(), end=previous_df['Date'].max(), freq="D").strftime("%Y-%m-%d").tolist()
    dates_df = pd.DataFrame(dates_list, columns=['Date'])

    df_currencies = pd.merge(df_currencies, dates_df, on='Date', how='right')

    for i in df_currencies.index:

        if ((pd.isna(df_currencies.loc[i, 'EURUSD=X'])) and (pd.isna(df_currencies.loc[i, 'EURGBP=X'])) and
            (pd.isna(df_currencies.loc[i, 'GBPUSD=X'])) and (pd.isna(df_currencies.loc[i, 'GBPEUR=X'])) and
            (pd.isna(df_currencies.loc[i, 'GBP=X'])) and (pd.isna(df_currencies.loc[i, 'EUR=X']))):

            df_currencies.loc[i, 'EURUSD=X'] = df_currencies.loc[i - 1, 'EURUSD=X']
            df_currencies.loc[i, 'EURGBP=X'] = df_currencies.loc[i - 1, 'EURGBP=X']
            df_currencies.loc[i, 'GBPUSD=X'] = df_currencies.loc[i - 1, 'GBPUSD=X']
            df_currencies.loc[i, 'GBPEUR=X'] = df_currencies.loc[i - 1, 'GBPEUR=X']
            df_currencies.loc[i, 'GBP=X'] = df_currencies.loc[i - 1, 'GBP=X']
            df_currencies.loc[i, 'EUR=X'] = df_currencies.loc[i - 1, 'EUR=X']

    df_currencies.to_csv(os.path.join(BASE_DIR, 'databases\Currencies Rate.csv'), sep=';', index=False)