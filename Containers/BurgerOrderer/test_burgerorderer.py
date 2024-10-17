import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    client = app.test_client()
    yield client

def test_get_menu(client):
    response = client.get('/menu')
    assert response.status_code == 200
    data = response.get_json()
    assert 'burgers' in data
    assert 'drinks' in data
    assert 'condiments' in data

def test_place_order(client):
    order_data = {'burger': 'Cheeseburger', 'drink': 'Cola'}
    response = client.post('/order', json=order_data)
    assert response.status_code == 200
    data = response.get_json()
    
    assert data['status'] == 'Order received and forwarded'

def test_search_menu(client):
    response = client.get('/search?q=Cheeseburger')
    assert response.status_code == 200
    data = response.get_json()
    assert 'burgers' in data
