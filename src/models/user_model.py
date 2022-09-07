from typing import List
from pydantic import BaseModel, Field, EmailStr

class UserModel(BaseModel):
    email: EmailStr = Field(...)
    password: str = Field(...)
    # friends: List[EmailStr]

    class Config:
        schema_extra = {
            "example": {
                "email":"email@test.com",
                "password":"pass123",
            }
        }
