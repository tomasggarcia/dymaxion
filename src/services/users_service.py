from typing import Optional
from src.repositories.user_repository import UserRepository
from src.models.user_model import UserModel

class UserService():
    repository = UserRepository()
    
    async def create_user(self, user: UserModel) -> Optional[UserModel]:
        existing_user: UserModel = await self.repository.find_by_email(user['email'])
        if existing_user is None:
            return await self.repository.create(user)
        return None

    async def delete_user(self, email) -> bool:
        deleted_documents: int = await self.repository.delete_by_email(email)
        if deleted_documents > 0:
            return True
        return False

    
    async def get_friend_list(self, email: str):
        user: UserModel = await self.repository.find_by_email(email)
        return user.friends