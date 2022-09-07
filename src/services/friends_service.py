from typing import Optional
from src.models.friends_model import FriendRequestsModel
from src.models.user_model import UserModel
from src.repositories.user_repository import UserRepository
from src.repositories.friend_repository import FriendRepository

class FriendService():
    friend_repository = FriendRepository()
    user_repository = UserRepository()
          
    async def create_friend_request(self, requester_user_email: str, requested_user_email: str):

        existing_requester_user: UserModel = await self.user_repository.find_by_email(requester_user_email)
        existing_requested_user: UserModel = await self.user_repository.find_by_email(requested_user_email)

        if existing_requester_user is None or existing_requested_user is None:
            return {'created': False, "message":"User does not exist"}

        existing_friend_request = await self.friend_request_exist(requester_user_email=existing_requester_user.email,requested_user_email=existing_requested_user.email)
        
        if existing_friend_request is not None:
            return {'created': False, "message":"Friend request already exist"}

        created_friend_request = await self.friend_repository.create(requester_user=existing_requester_user,requested_user=existing_requested_user)
        if created_friend_request:
            return {'created': True, "created_request": created_friend_request}

    async def friend_request_exist(self, requester_user_email, requested_user_email) -> Optional[FriendRequestsModel]:
        friend_request: FriendRequestsModel = await self.friend_repository.find_friend_request(requester_user_email,requested_user_email)
        if friend_request:
            return friend_request
        return None