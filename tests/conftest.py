from main import app
from src.config.database import db
from pytest import fixture
from src.repositories.user_repository import UserRepository
import pytest
import asyncio
# friends_db = db["friends"]
# users_db = db["users"]

@pytest.fixture(scope="session")
def event_loop():
    return asyncio.get_event_loop()

@fixture(scope="session", autouse=True)
async def test_client():
    await db['users'].drop()
    await db['friends'].drop()
    await db['room'].drop()