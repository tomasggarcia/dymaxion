from pydantic import BaseModel, Field
from src.models.user_model import UserModel
from enum import IntEnum

class StatusEnum(IntEnum):
    requested = 0
    accepted = 1
    rejected = 2

class FriendRequestsModel(BaseModel):
    requester_user_email: str = Field(...)
    requested_user_email: str = Field(...)
    status: StatusEnum = StatusEnum.requested

    class Config:
        schema_extra = {
            "example": {
                "requester_user_email":"email@test.com",
                "requested_user_email":"emaild@test.com",
            }
        }
