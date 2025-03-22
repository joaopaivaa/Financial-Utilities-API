from fastapi.testclient import TestClient
from main import app
from fastapi import status

client = TestClient(app)

def test_french_amortization_route():

    data = {
        'principal': 1000,
        'rate': 0.05,
        'periods': 5
    }
    response = client.post('/french_amortization', json=data)
    assert response.status_code == status.HTTP_200_OK
    response_json = response.json()
    assert 'Period' in response_json
    assert len(response_json['Period']) > 0
    assert 'Payment' in response_json
    assert len(response_json['Payment']) > 0
    assert 'Interest' in response_json
    assert len(response_json['Interest']) > 0
    assert 'Principal' in response_json
    assert len(response_json['Principal']) > 0
    assert 'Balance' in response_json
    assert len(response_json['Balance']) > 0

def test_sac_amortization_route():
    data = {
        'principal': 1000,
        'rate': 0.05,
        'periods': 5
    }
    response = client.post('/sac_amortization', json=data)
    assert response.status_code == status.HTTP_200_OK
    response_json = response.json()
    assert 'Period' in response_json
    assert len(response_json['Period']) > 0
    assert 'Payment' in response_json
    assert len(response_json['Payment']) > 0
    assert 'Interest' in response_json
    assert len(response_json['Interest']) > 0
    assert 'Principal' in response_json
    assert len(response_json['Principal']) > 0
    assert 'Balance' in response_json
    assert len(response_json['Balance']) > 0