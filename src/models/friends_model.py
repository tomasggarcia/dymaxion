from pydantic import BaseModel
from src.models.user_model import UserModel
from enum import IntEnum

class StatusEnum(IntEnum):
    requested = 0
    accepted = 1
    rejected = 2

class FriendRequestsModel(BaseModel):
    requester_user_email: str
    requested_user_email: str
    status: StatusEnum = StatusEnum.requested
