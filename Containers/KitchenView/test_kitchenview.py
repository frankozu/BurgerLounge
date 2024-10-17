import pytest
from appk import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_receive_order(client):
    """Test the /order endpoint"""
    order_data = {'burger': 'Cheeseburger', 'drink': 'Cola'}
    response = client.post('/order', json=order_data)
    assert response.status_code == 200
    assert response.get_json()['status'] == 'Order received by KitchenView'
