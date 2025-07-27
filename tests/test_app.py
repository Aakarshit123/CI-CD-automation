import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from app import app

def test_home():
    client = app.test_client()
    response = client.get('/')
    assert response.status_code == 200

def test_health():
    client = app.test_client()
    response = client.get('/health')
    assert response.status_code == 200

def test_users():
    client = app.test_client()
    response = client.get('/api/users')
    assert response.status_code == 200
    assert b"Jibbran" in response.data
