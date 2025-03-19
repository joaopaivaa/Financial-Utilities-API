import yfinance as yf
import pandas as pd
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

eur_usd = yf.download(['EURUSA=X'], period='max')

eur_gbp = yf.download(['EURGBP=X'], period='max')

gbp_usd = yf.download(['GBPUSD=X'], period='max')

gbp_eur = yf.download(['GBPEUR=X'], period='max')

usd_gbp = yf.download(['GBP=X'], period='max')

usd_eur = yf.download(['EUR=X'], period='max')

df_currencies = pd.DataFrame({'EUR-USD': eur_usd,
                              'EUR-GBP': eur_gbp,
                              'GBP-USD': gbp_usd,
                              'GBP-EUR': gbp_eur,
                              'USD-GBP': usd_gbp,
                              'USD-EUR': usd_eur})

df_currencies.to_csv(os.path.join(BASE_DIR, 'Currencies Rate.csv'), sep=';', index=False)
