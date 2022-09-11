from main import app
import pytest
from httpx import AsyncClient
import os
from tests.conftest import add_users

url = os.getenv("BACKEND_URL")

@pytest.mark.asyncio
async def test_create_chat_room(add_users):
    async with AsyncClient(app=app, base_url=url) as ac:
        response = await ac.post("/new-room",json=["email@test.com", "emaild@test.com"])
    assert response.status_code == 201