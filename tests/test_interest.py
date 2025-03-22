from fastapi.testclient import TestClient
from main import app
from fastapi import status

client = TestClient(app)

def test_simple_interest_route_time():

    data = {
        'amount': 10000,
        'principal': 1000,
        'rate': 0.05
    }
    response = client.post('/simple_interest', json=data)
    assert response.status_code == status.HTTP_200_OK
    response_json = response.json()
    assert 'time' in response_json

def test_simple_interest_route_rate():

    data = {
        'amount': 10000,
        'principal': 1000,
        'time': 1
    }
    response = client.post('/simple_interest', json=data)
    assert response.status_code == status.HTTP_200_OK
    response_json = response.json()
    assert 'rate' in response_json

def test_simple_interest_route_principal():

    data = {
        'amount': 10000,
        'rate': 0.05,
        'time': 2
    }
    response = client.post('/simple_interest', json=data)
    assert response.status_code == status.HTTP_200_OK
    response_json = response.json()
    assert 'principal' in response_json
    assert response_json['principal'] < data['amount']

def test_simple_interest_route_amount():

    data = {
        'principal': 1000,
        'rate': 0.05,
        'time': 2
    }
    response = client.post('/simple_interest', json=data)
    assert response.status_code == status.HTTP_200_OK
    response_json = response.json()
    assert 'amount' in response_json
    assert data['principal'] < response_json['amount']

def test_compound_interest_route_time():

    data = {
        'amount': 10000,
        'principal': 1000,
        'rate': 0.05
    }
    response = client.post('/compound_interest', json=data)

    assert response.status_code == status.HTTP_200_OK
    response_json = response.json()
    assert 'time' in response_json

def test_compound_interest_route_rate():

    data = {
        'amount': 10000,
        'principal': 1000,
        'time': 1
    }
    response = client.post('/compound_interest', json=data)

    assert response.status_code == status.HTTP_200_OK
    response_json = response.json()
    assert 'rate' in response_json

def test_compound_interest_route_principal():

    data = {
        'amount': 10000,
        'rate': 0.05,
        'time': 2
    }
    response = client.post('/compound_interest', json=data)
    assert response.status_code == status.HTTP_200_OK
    response_json = response.json()
    assert 'principal' in response_json
    assert response_json['principal'] < data['amount']

def test_compound_interest_route_amount():

    data = {
        'principal': 1000,
        'rate': 0.05,
        'time': 2
    }
    response = client.post('/compound_interest', json=data)
    assert response.status_code == status.HTTP_200_OK
    response_json = response.json()
    assert 'amount' in response_json
    assert data['principal'] < response_json['amount']
