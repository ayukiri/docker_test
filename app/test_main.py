# app/test_main.py

from main import app

def test_home():
    client = app.test_client()
    response = client.get('/')
    assert response.status_code == 200
    assert b'Hello, Flask!' in response.data
