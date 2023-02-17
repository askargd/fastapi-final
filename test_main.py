from fastapi.testclient import TestClient
from fastapi import status
from main import app

client = TestClient(app=app)


def test_get_sum1n():
    response = client.get("/sum1n/5")
    assert response.status_code == 200

    
def test_get_fibo():
    response = client.get("/fibo?n=5")
    assert response.status_code == 200
    
def test_post():
    response = client.post('/reverse?string',json={'string': 'Hello'})
    assert response.status_code == 200

def test_put_list():
    response = client.put('/list/{element}',json={'element':'Apple','element':'Microsoft'})
    assert response.status_code == 200

def get_list():
    response = client.get('/list')
    assert response.status_code == 200

    data = response.json()
    print(data)

def test_calculator():
    response = client.post('/calculator',json={"expr": "5,+,6"})
    assert response.status_code == 200
    response = client.post('/calculator',json={"expr": "5,-,6"})
    assert response.status_code == 200
    response = client.post('/calculator',json={"expr": "5,*,6"})
    assert response.status_code == 200
    response = client.post('/calculator',json={"expr": "5,/,6"})
    assert response.status_code == 200
    response = client.post('/calculator',json={"expr": "5,/,0"})
    assert response.status_code == 403
    response = client.post('/calculator',json={"expr": "5,string,0"})
    assert response.status_code == 400
    

