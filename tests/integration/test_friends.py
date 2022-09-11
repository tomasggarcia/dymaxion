from main import app
import pytest
from httpx import AsyncClient
import os

from tests.conftest import add_users

url = os.getenv("BACKEND_URL")

@pytest.mark.asyncio
async def test_create_friend_request(add_users):
    async with AsyncClient(app=app, base_url=url) as ac:
        response = await ac.post("/friends",json={
            "requester_user_email": "email@test.com",
            "requested_user_email": "emaild@test.com"
        })
    assert response.status_code == 201
    assert response.json() == {
        "response": {
            "created": True,
            "created_request": {
            "requester_user_email": "email@test.com",
            "requested_user_email": "emaild@test.com",
            "status": 0
            }
        }
    }

@pytest.mark.asyncio
async def test_accept_friend_request():
    async with AsyncClient(app=app, base_url=url) as ac:
        response = await ac.put("/friends/accept",json={
            "requester_user_email": "email@test.com",
            "requested_user_email": "emaild@test.com"
        })
    assert response.json() == {
        "response": {
            "updated": True,
            "message": "Friend request accepted"
        }
    }
    assert response.status_code == 202