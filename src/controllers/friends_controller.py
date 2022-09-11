from main import app
from src.services.users_service import UserService
from src.models.friends_model import FriendRequestsModel
from src.services.friends_service import FriendService
from fastapi.encoders import jsonable_encoder
from fastapi import status
from fastapi.responses import JSONResponse

friend_service = FriendService()


@app.post("/friends")
async def create_friend_request(friend_request: FriendRequestsModel):
    friend_request = jsonable_encoder(friend_request)
    requester_user_email = friend_request['requester_user_email']
    requested_user_email = friend_request['requested_user_email']
    if requester_user_email == requested_user_email:
        return JSONResponse(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, content=jsonable_encoder({"response": "Emails cannot be equal"}))      
    create_response = await friend_service.create_friend_request(requester_user_email, requested_user_email)
    if create_response['created'] is False:
        return JSONResponse(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, content=jsonable_encoder({"response": create_response['message']}))
    return JSONResponse(status_code=status.HTTP_201_CREATED, content=jsonable_encoder({"response": create_response}))


@app.put("/friends/accept")
async def accept_friend_request(friend_request: FriendRequestsModel):
    friend_request = jsonable_encoder(friend_request)
    requester_user_email = friend_request['requester_user_email']
    requested_user_email = friend_request['requested_user_email']
    if requester_user_email == requested_user_email:
        return JSONResponse(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, content=jsonable_encoder({"response": "Emails cannot be equal"}))      
    updated_friend_request = await friend_service.accept_friend_request(requester_user_email,requested_user_email)
    if updated_friend_request['updated'] is False:
        return JSONResponse(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, content=jsonable_encoder({"response": updated_friend_request['message']}))
    return JSONResponse(status_code=status.HTTP_202_ACCEPTED, content=jsonable_encoder({"response": updated_friend_request}))


@app.put("/friends/reject")
async def accept_friend_request(friend_request: FriendRequestsModel):
    friend_request = jsonable_encoder(friend_request)
    requester_user_email = friend_request['requester_user_email']
    requested_user_email = friend_request['requested_user_email']
    if requester_user_email == requested_user_email:
        return JSONResponse(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, content=jsonable_encoder({"response": "Emails cannot be equal"}))      
    service = FriendService()
    updated_friend_request = await friend_service.reject_friend_request(requester_user_email,requested_user_email)
    if updated_friend_request['updated'] is False:
        return JSONResponse(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, content=jsonable_encoder({"response": updated_friend_request['message']}))
    return JSONResponse(status_code=status.HTTP_202_ACCEPTED, content=jsonable_encoder({"response": updated_friend_request}))

@app.delete("/friends")
async def accept_friend_request(requester_user_email, requested_user_email):
    if requester_user_email == requested_user_email:
        return JSONResponse(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, content=jsonable_encoder({"response": "Emails cannot be equal"}))      
    service = FriendService()
    service_response = await friend_service.remove_friend(requester_user_email,requested_user_email)
    if service_response['deleted'] is False:
        return JSONResponse(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, content=jsonable_encoder({"response": service_response['message']}))      
    return JSONResponse(status_code=status.HTTP_202_ACCEPTED, content=jsonable_encoder({"response": service_response['message']}))      

