from fastapi.testclient import TestClient
from main import app
import pytest
from httpx import AsyncClient
import os

url = os.getenv("BACKEND_URL")

@pytest.mark.asyncio
async def test_create_user():
    async with AsyncClient(app=app, base_url=url) as ac:
        response = await ac.post("/users",json={
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

@pytest.mark.asyncio
async def test_delete_user():
    async with AsyncClient(app=app, base_url=url) as ac:
        response = await ac.delete("/users", params={"user_email":"email@test.com"})
    assert response.status_code == 200
    assert response.json() == {"response": "User deleted succesfully"}