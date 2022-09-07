from src.models.user_model import UserModel
from src.repositories.user_repository import UserRepository
from src.repositories.friend_repository import FriendRepository

class FriendService():
    async def create_friend_request(self, requester_user_email: str, requested_user_email: str):
        friend_repository = FriendRepository()
        user_repository = UserRepository()
        existing_requester_user: UserModel = await user_repository.find_by_email(requester_user_email)
        existing_requested_user: UserModel = await user_repository.find_by_email(requested_user_email)
        print(existing_requester_user)
        print(existing_requested_user)
        if existing_requester_user is None or existing_requested_user is None:
            return False
        # response = await friend_repository.create(requester_user=existing_requester_user,requested_user=existing_requested_user)
        return True