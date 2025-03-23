import yfinance as yf
import pandas as pd
import os
from datetime import datetime, timedelta

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

    df_currencies.to_csv(os.path.join(BASE_DIR, 'databases\Currencies Rate.csv'), sep=';', index=True)
