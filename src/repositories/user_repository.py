from typing import Any, Optional
from src.config.database import db
from src.models.user_models import UserModel

class UserRepository():

    async def create(self, user:UserModel) -> Optional[UserModel]:
        new_user = await db["users"].insert_one(user)
        return await self.get_by_id(new_user.inserted_id)

    async def find_by_email(self, email: str) -> Optional[UserModel]:
        return await self.get_by({'email':email})

    async def get_by_id(self, id:Any) -> UserModel:
        return await self.get_by({'_id':id})

    async def get_by(self, filter: dict) -> UserModel:
        user = await db["users"].find_one(filter)
        return UserModel(**user) if user is not None else None

    async def delete_by_email(self, email: str) -> int:
        delete_result_object =  await db["users"].delete_one({'email':email})
        return delete_result_object.deleted_count