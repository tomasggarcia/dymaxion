from typing import Optional
from src.models.friends_model import FriendRequestsModel, StatusEnum
from src.models.user_model import UserModel
from src.repositories.user_repository import UserRepository
from src.repositories.friend_repository import FriendRepository

class FriendService():
    friend_repository = FriendRepository()
    user_repository = UserRepository()
          
    async def create_friend_request(self, requester_user_email: str, requested_user_email: str):

        existing_requester_user: UserModel = await self._user_exists(requester_user_email)
        existing_requested_user: UserModel = await self._user_exists(requested_user_email)
        if existing_requester_user is None or existing_requested_user is None:
            return {'created': False, "message":"User does not exist"}

        existing_friend_request = await self._friend_request_exist(requester_user_email=existing_requester_user.email,requested_user_email=existing_requested_user.email)
        if existing_friend_request is not None:
            return {'created': False, "message":"Friend request already exist"}

        created_friend_request = await self.friend_repository.create(requester_user=existing_requester_user,requested_user=existing_requested_user)
        if created_friend_request:
            return {'created': True, "created_request": created_friend_request}

    async def accept_friend_request(self, requester_user_email, requested_user_email):
        return await self._update_friend_request(requester_user_email, requested_user_email, status=StatusEnum.accepted)

    async def reject_friend_request(self, requester_user_email, requested_user_email):
        return await self._update_friend_request(requester_user_email, requested_user_email, status=StatusEnum.rejected)

    async def remove_friend(self, requester_user_email, requested_user_email):
        existing_friend_request = await self._friend_request_exist(requester_user_email,requested_user_email)
        if existing_friend_request is None:
            return {'deleted': False, "message": "User is not in friends list"}
        if existing_friend_request.status == StatusEnum.accepted:
            deleted_request = await self.friend_repository.remove(requester_user_email, requested_user_email)
            if deleted_request > 0:
                return {'deleted': True, "message": "user removed from friends list"}
            return {'deleted': False, "message": "Could not remove user from friend list"}
        return {'deleted': False, "message": "User is not in friends list"}

    async def _update_friend_request(self, requester_user_email, requested_user_email, status):
        existing_requester_user: UserModel = await self._user_exists(requester_user_email)
        existing_requested_user: UserModel = await self._user_exists(requested_user_email)
        if existing_requester_user is None or existing_requested_user is None:
            return {'updated': False, "message":"User does not exist"}
    
        existing_friend_request = await self._friend_request_exist(requester_user_email=existing_requester_user.email,requested_user_email=existing_requested_user.email)
        if existing_friend_request is None:
            return {'updated': False, "message":"Friend request does not exist"}
        updated_friend_request = await self.friend_repository.update_friend_request(requester_user_email,requested_user_email,status)
        
        if updated_friend_request.status == StatusEnum.accepted:
            await self._add_friend(updated_friend_request.requester_user_email, updated_friend_request.requested_user_email)
        
        return {'updated': True, 'updated_request':updated_friend_request}


    async def _add_friend(self, user_email, friend_email):
        requester_user: UserModel = await self.user_repository.find_by_email(user_email)
        if requester_user:
            await self.user_repository.add_friend(requester_user.email, friend_email)
        return
    async def _user_exists(self, email) -> Optional[UserModel]:
            return await self.user_repository.find_by_email(email)

    async def _friend_request_exist(self, requester_user_email, requested_user_email) -> Optional[FriendRequestsModel]:
        friend_request: FriendRequestsModel = await self.friend_repository.find_friend_request(requester_user_email,requested_user_email)
        return friend_request