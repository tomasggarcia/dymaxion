import email
from src.models.friends_model import FriendRequestsModel
from src.repositories.user_repository import UserRepository
from src.repositories.friend_repository import FriendRepository
from src.services.friends_service import FriendService
from src.models.user_model import UserModel
from pydantic_factories import ModelFactory
import pytest

class TestFriends:
    friend_service = FriendService()
    
    friend_repository = FriendRepository()
    user_repository = UserRepository()

    class UserFactory(ModelFactory):
        __model__ = UserModel
        email = "email@test.com"
        password="pass123"
        friends=["email@test.com"]

    class FriendFactory(ModelFactory):
        __model__ = FriendRequestsModel
        requester_user_email= "email@test.com"
        requested_user_email= "emaild@test.com"
        status: 0

    async def test_create_friend_request_invalid_user(self, mocker):
        mocker.patch("src.repositories.user_repository.UserRepository.find_by_email", return_value = None)
        response = await self.friend_service.create_friend_request(requester_user_email="email@test.com", requested_user_email="emaild@test.com")
        assert response == {'created': False, "message":"User does not exist"}

    async def test_create_friend_request_already_friends(self, mocker):
        mock_user = self.UserFactory()
        mocker.patch("src.repositories.user_repository.UserRepository.find_by_email", return_value = mock_user)
        response = await self.friend_service.create_friend_request(requested_user_email="email@test.com", requester_user_email="emaild@test.com")
        assert response == {'created': False, "message": "Users already friends"}

    async def test_create_friend_request_request_already_exist(self, mocker):
        mock_user = self.UserFactory()
        mock_user.friends = []
        mock_friend_request = self.FriendFactory()
        mocker.patch("src.repositories.user_repository.UserRepository.find_by_email", return_value = mock_user)
        mocker.patch("src.repositories.friend_repository.FriendRepository.find_friend_request", return_value = mock_friend_request)
        response = await self.friend_service.create_friend_request(requested_user_email="email@test.com", requester_user_email="emaild@test.com")
        assert response == {'created': False, "message":"Friend request already exist"}

    async def test_create_friend_request(self, mocker):
        mock_user = self.UserFactory()
        mock_user.friends = []
        mocker.patch("src.repositories.user_repository.UserRepository.find_by_email", return_value = mock_user)
        response = await self.friend_service.create_friend_request(requested_user_email="email@test.com", requester_user_email="emaild@test.com")
        assert response == {'created': True, "created_request": {
            "requester_user_email": "email@test.com",
            "requested_user_email": "email@test.com",
            "status": 0
        }}