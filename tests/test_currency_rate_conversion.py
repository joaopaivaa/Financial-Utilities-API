from fastapi.testclient import TestClient
from main import app
from fastapi import status

client = TestClient(app)

def test_currency_rate_conversion_EUR():

    data = {
        'dates': ['2020/01/01', '2020/02/01', '2020/03/01', '2020/04/01', '2020/05/01'],
        'values': [1, 1, 1, 1, 1],
        'original_currency': 'EUR'
    }
    response = client.post('/currency_rate_conversion', json=data)
    assert response.status_code == status.HTTP_200_OK
    response_json = response.json()
    assert 'USD' in response_json
    assert len(response_json['USD']) > 0
    assert 'GBP' in response_json
    assert len(response_json['GBP']) > 0

def test_currency_rate_conversion_GBP():

    data = {
        'dates': ['2020/01/01', '2020/02/01', '2020/03/01', '2020/04/01', '2020/05/01'],
        'values': [1, 1, 1, 1, 1],
        'original_currency': 'GBP'
    }
    response = client.post('/currency_rate_conversion', json=data)
    assert response.status_code == status.HTTP_200_OK
    response_json = response.json()
    assert 'USD' in response_json
    assert len(response_json['USD']) > 0
    assert 'EUR' in response_json
    assert len(response_json['EUR']) > 0

def test_currency_rate_conversion_USD():

    data = {
        'dates': ['2020/01/01', '2020/02/01', '2020/03/01', '2020/04/01', '2020/05/01'],
        'values': [1, 1, 1, 1, 1],
        'original_currency': 'USD'
    }
    response = client.post('/currency_rate_conversion', json=data)
    assert response.status_code == status.HTTP_200_OK
    response_json = response.json()
    assert 'EUR' in response_json
    assert len(response_json['EUR']) > 0
    assert 'GBP' in response_json
    assert len(response_json['GBP']) > 0