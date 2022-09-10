from src.models.friends_model import FriendRequestsModel, StatusEnum
from src.models.user_model import UserModel
from src.config.database import db

class FriendRepository():
    friends_db = db["friends"]

    async def create(self, requester_user: UserModel, requested_user: FriendRequestsModel):
        new_friend_request = await self.friends_db.insert_one({'requester_user_email': requester_user.email, 'requested_user_email': requested_user.email})
        return await self.get_by_id(new_friend_request.inserted_id)

    async def find_requester_by_email(self, id) -> FriendRequestsModel:
        return await self.get_by({'requester_user_id': id})

    async def find_requested_by_email(self, id) -> FriendRequestsModel:
        return await self.get_by({'requested_user_id': id})

    async def find_friend_request(self, requester_user_email, requested_user_email) -> FriendRequestsModel:
        return await self.get_by({'requester_user_email': requester_user_email, 'requested_user_email': requested_user_email})

    async def get_by_id(self, id) -> FriendRequestsModel:
        return await self.get_by({'_id':id})
    
    async def update_friend_request(self, requester_user_email, requested_user_email, status):
        await self.friends_db.update_one(
            {'requester_user_email': requester_user_email,'requested_user_email': requested_user_email},
            {'$set':{'status': status}}
        )
        return await self.get_by({'requester_user_email': requester_user_email, 'requested_user_email': requested_user_email})

    async def remove(self, requester_user_email, requested_user_email):
        delete_result_object =  await self.friends_db.delete_one({'requester_user_email':requester_user_email,'requested_user_email':requested_user_email})
        return delete_result_object.deleted_count

    async def get_by(self, filter: dict) -> FriendRequestsModel:
        friend_request = await self.friends_db.find_one(filter)
        return FriendRequestsModel(**friend_request) if friend_request is not None else None
