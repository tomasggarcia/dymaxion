from pydantic import BaseModel
from src.models.user_model import UserModel
from enum import IntEnum

class StatusEnum(IntEnum):
    requested: 0
    accepted: 1
    rejected: 2

class FriendRequestsModel(BaseModel):
    requester_user_id: UserModel
    requested_user_id: UserModel
    status: StatusEnum = StatusEnum.requested
