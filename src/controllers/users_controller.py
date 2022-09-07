from main import app
from src.models.user_models import UserModel
from src.services.users_service import UserService
from fastapi.encoders import jsonable_encoder
from fastapi import status, Response

@app.post("/users", response_description="User added", status_code=status.HTTP_201_CREATED)
async def create_user(user: UserModel, response: Response):
    user = jsonable_encoder(user)
    service = UserService()
    new_user = await service.create_user(user)
    if new_user is None:
        response.status_code = status.HTTP_409_CONFLICT
        return {"User already exists"}
    return {"results": new_user}