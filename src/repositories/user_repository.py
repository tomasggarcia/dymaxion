from typing import Any, Optional
from src.config.database import db
from src.models.user_model import UserModel

class UserRepository():
    user_db = db["users"]

    async def create(self, user:UserModel) -> Optional[UserModel]:
        new_user = await self.user_db.insert_one(user)
        return await self.get_by_id(new_user.inserted_id)

    async def add_friend(self, user_email, friend_email):
        requester_user: UserModel = await self.find_by_email(user_email)
        if requester_user:
            await self.user_db.update_one(
                {'email': user_email},
                {'$addToSet':{'friends': friend_email}}
            )

    async def remove_friend(self, user_email, friend_email):
        requester_user: UserModel = await self.find_by_email(user_email)
        if requester_user:
            await self.user_db.update_one(
                {'email': user_email},
                {'$pull':{'friends': friend_email}}
            )

    async def find_by_email(self, email: str) -> Optional[UserModel]:
        return await self.get_by({'email':email})

    async def get_by_id(self, id:Any) -> UserModel:
        return await self.get_by({'_id':id})

    async def get_by(self, filter: dict) -> UserModel:
        user = await self.user_db.find_one(filter)
        return UserModel(**user) if user is not None else None

    async def delete_by_email(self, email: str) -> int:
        delete_result_object =  await self.user_db.delete_one({'email':email})
        return delete_result_object.deleted_count