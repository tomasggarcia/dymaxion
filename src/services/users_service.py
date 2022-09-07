from typing import Optional
from src.repositories.user_repository import UserRepository
from src.models.user_models import UserModel

class UserService():
    async def create_user(self, user: UserModel) -> Optional[UserModel]:
        repository = UserRepository()
        existing_user = await repository.find_by_email(user['email'])
        if existing_user is None:
            return await repository.create(user)
        return None
