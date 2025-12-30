from fastapi.testclient import TestClient
from main import app
from fastapi import status
import pandas as pd

client = TestClient(app)

def test_BRL_inflation_adjustment_route():

    data = {
        'dates': ['2000/01/01', '2010/01/01', '2020/01/01', '2025/01/01'],
        'values': [100] * 4,
        'currency': 'BRL',
        'present_date': '2025/11/01'
    }
    response = client.post('/inflation_adjustment', json=data)

    assert response.status_code == status.HTTP_200_OK
    response_json = response.json()

    df_response = pd.DataFrame(response_json)
    df_response['Date'] = pd.to_datetime(df_response['Date'])

    assert len(df_response) > 0
    assert all(col in df_response.columns for col in ['Date', 'Value', 'Accumulated Inflation (%)', 'Adjusted Value'])
    assert df_response[df_response['Date'] == '2025-01-01']['Adjusted Value'].values[0] == 103.76

    # Reference: https://sidra.ibge.gov.br/Tabela/1737


def test_GBP_inflation_adjustment_route():

    data = {
        'dates': ['2000/01/01', '2010/01/01', '2020/01/01', '2025/01/01'],
        'values': [100] * 4,
        'currency': 'GBP',
        'present_date': '2025/11/01'
    }
    response = client.post('/inflation_adjustment', json=data)

    assert response.status_code == status.HTTP_200_OK
    response_json = response.json()
    
    df_response = pd.DataFrame(response_json)
    df_response['Date'] = pd.to_datetime(df_response['Date'])

    assert len(df_response) > 0
    assert all(col in df_response.columns for col in ['Date', 'Value', 'Accumulated Inflation (%)', 'Adjusted Value'])
    assert df_response[df_response['Date'] == '2025-01-01']['Adjusted Value'].values[0] == 103.03

    # Reference: https://www.ons.gov.uk/economy/inflationandpriceindices/timeseries/d7bt/mm23?referrer=search&searchTerm=d7bt


def test_USD_inflation_adjustment_route():

    data = {
        'dates': ['2000/01/01', '2010/01/01', '2020/01/01', '2025/01/01'],
        'values': [100] * 4,
        'currency': 'USD',
        'present_date': '2025/11/01'
    }
    response = client.post('/inflation_adjustment', json=data)

    assert response.status_code == status.HTTP_200_OK
    response_json = response.json()
    
    df_response = pd.DataFrame(response_json)
    df_response['Date'] = pd.to_datetime(df_response['Date'])

    assert len(df_response) > 0
    assert all(col in df_response.columns for col in ['Date', 'Value', 'Accumulated Inflation (%)', 'Adjusted Value'])
    assert df_response[df_response['Date'] == '2025-01-01']['Adjusted Value'].values[0] == 102.03

    # Reference: https://data.bls.gov/timeseries/CUUR0000SA0