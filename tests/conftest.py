from main import app
from src.config.database import db
from pytest import fixture
from src.repositories.user_repository import UserRepository
import pytest
import asyncio


friends_db = db["friends"]
users_db = db["users"]
rooms_db = db["room"]

@pytest.fixture(scope="session")
def event_loop():
    return asyncio.get_event_loop()

@fixture(scope="module", autouse=True)
async def initial():
    await users_db.drop()
    await friends_db.drop()
    await rooms_db.drop()


@fixture(scope="module")
async def add_users():
    user_repository = UserRepository()
    await user_repository.create(user={
        "email": "email@test.com",
        "password": "pass123"
    })
    await user_repository.create(user={
        "email": "emaild@test.com",
        "password": "pass123"
    })