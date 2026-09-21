import pytest
from app import application

@pytest.fixture
def client():
    application.config['TESTING'] = True
    with application.test_client() as client:
        yield client

def test_home(client):
    response = client.get('/')
    assert response.status_code == 200
    assert response.json['service_name'] == "CloudKart Core Engine"

def test_health(client):
    response = client.get('/health')
    assert response.status_code == 200
    assert response.json['status'] == "healthy"
