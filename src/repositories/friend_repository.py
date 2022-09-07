
from src.models.friends_model import FriendRequestsModel
from src.models.user_model import UserModel
from src.config.database import db

class FriendRepository():

    async def create(self, requester_user: UserModel, requested_user: UserModel):
        new_friend_request = await db["friends"].insert_one({'requester_user_id': requester_user, 'requested_user_id': requested_user})
        return await new_friend_request

    async def find_requester_by_email(self, id) -> FriendRequestsModel:
        return await db['friends'].find_one({'requester_user_id': id})

    async def get_by_id(self, id) -> FriendRequestsModel:
        return await self.get_by({'_id':id})
