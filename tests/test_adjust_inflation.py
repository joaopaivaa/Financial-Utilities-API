from fastapi.testclient import TestClient
from main import app
from fastapi import status
import pandas as pd

client = TestClient(app)

def test_BRL_inflation_adjustment_route():

    data = {
        'dates': ['2000/01/01', '2010/01/01', '2020/01/01'],
        'values': [100, 100, 100],
        'currency': 'BRL',
        'present_date': '2025/01/01'
    }
    response = client.post('/inflation_adjustment', json=data)

    assert response.status_code == status.HTTP_200_OK
    response_json = response.json()

    df_response = pd.DataFrame(response_json)
    df_response['Date'] = pd.to_datetime(df_response['Date'])

    assert len(df_response) > 0
    assert all(col in df_response.columns for col in ['Date', 'Value', 'Accumulated Inflation (%)', 'Adjusted Value - 2025-01-01'])


def test_GBP_inflation_adjustment_route():

    data = {
        'dates': ['2000/01/01', '2010/01/01', '2020/01/01'],
        'values': [100, 100, 100],
        'currency': 'GBP',
        'present_date': '2025/01/01'
    }
    response = client.post('/inflation_adjustment', json=data)

    assert response.status_code == status.HTTP_200_OK
    response_json = response.json()
    
    df_response = pd.DataFrame(response_json)
    df_response['Date'] = pd.to_datetime(df_response['Date'])

    assert len(df_response) > 0
    assert all(col in df_response.columns for col in ['Date', 'Value', 'Accumulated Inflation (%)', 'Adjusted Value - 2025-01-01'])


def test_USD_inflation_adjustment_route():

    data = {
        'dates': ['2000/01/01', '2010/01/01', '2020/01/01'],
        'values': [100, 100, 100],
        'currency': 'USD',
        'present_date': '2025/01/01'
    }
    response = client.post('/inflation_adjustment', json=data)

    assert response.status_code == status.HTTP_200_OK
    response_json = response.json()
    
    df_response = pd.DataFrame(response_json)
    df_response['Date'] = pd.to_datetime(df_response['Date'])

    assert len(df_response) > 0
    assert all(col in df_response.columns for col in ['Date', 'Value', 'Accumulated Inflation (%)', 'Adjusted Value - 2025-01-01'])