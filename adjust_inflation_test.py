from fastapi.testclient import TestClient
from main import app
from fastapi import status

client = TestClient(app)

def test_BRL_adjust_inflation_route():

    data = {
        'dates': ['2020/01/01', '2020/02/01', '2020/03/01', '2020/04/01', '2020/05/01'],
        'values': [100, 150, 200, 250, 300],
        'currency': 'BRL',
        'present_date': '2025/03/20'
    }
    response = client.post('/adjust_inflation', json=data)

    assert response.status_code == status.HTTP_200_OK
    response_json = response.json()
    assert response_json == response_json

def test_GBP_adjust_inflation_route():

    data = {
        'dates': ['2020/01/01', '2020/02/01', '2020/03/01', '2020/04/01', '2020/05/01'],
        'values': [100, 150, 200, 250, 300],
        'currency': 'GBP',
        'present_date': '2025/03/20'
    }
    response = client.post('/adjust_inflation', json=data)

    assert response.status_code == status.HTTP_200_OK
    response_json = response.json()
    assert response_json == response_json

def test_Dollar_adjust_inflation_route():

    data = {
        'dates': ['2020/01/01', '2020/02/01', '2020/03/01', '2020/04/01', '2020/05/01'],
        'values': [100, 150, 200, 250, 300],
        'currency': 'Dollar',
        'present_date': '2025/03/20'
    }
    response = client.post('/adjust_inflation', json=data)

    assert response.status_code == status.HTTP_200_OK
    response_json = response.json()
    assert response_json == response_json
