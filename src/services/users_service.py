from typing import Optional
from src.repositories.user_repository import UserRepository
from src.models.user_model import UserModel

class UserService():
    async def create_user(self, user: UserModel) -> Optional[UserModel]:
        repository = UserRepository()
        existing_user = await repository.find_by_email(user['email'])
        if existing_user is None:
            return await repository.create(user)
        return None

    async def delete_user(self, email) -> bool:
        repository = UserRepository()
        deleted_documents: int = await repository.delete_by_email(email)
        if deleted_documents > 0:
            return True
        return False