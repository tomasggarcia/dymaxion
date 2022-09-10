from main import app
from src.models.user_model import UserModel
from src.services.users_service import UserService
from fastapi.encoders import jsonable_encoder
from fastapi import status, Body
from fastapi.responses import JSONResponse


user_service = UserService()

@app.post("/users", response_description="User added")
async def create_user(user: UserModel):
    user = jsonable_encoder(user)
    new_user = await user_service.create_user(user)
    if new_user is None:
        return JSONResponse(status_code=status.HTTP_409_CONFLICT, content=jsonable_encoder({"response": "User already exists"}))
    return JSONResponse(status_code=status.HTTP_201_CREATED, content=jsonable_encoder({"response": {"user": new_user}}))

@app.delete("/users")
async def delete_user(user_email: str = Body(example='email@test.com',embed=True)):
    delete_status = await user_service.delete_user(user_email)
    if delete_status:
        return JSONResponse(status_code=status.HTTP_200_OK, content=jsonable_encoder({"response": "User deleted succesfully"}))
    return JSONResponse(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, content=jsonable_encoder({"response": "Email does not exist"}))