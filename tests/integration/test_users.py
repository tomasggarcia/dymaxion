from fastapi.testclient import TestClient
from main import app
import os

client = TestClient(app)

def test_read_main():
    response = client.post("/users",json={
        "email":"email@test.com",
        "password":"123"
    })
    assert response.status_code == 201
    assert response.json() == {"response": {
        "user": {
            "email":"email@test.com",
            "password":"123",
            "friends":[]
        }
    }}