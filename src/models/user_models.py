from pydantic import BaseModel, Field, EmailStr

class UserModel(BaseModel):
    email: EmailStr = Field(...)
    password: str = Field(...)

    class Config:
        schema_extra = {
            "example": {
                "email":"email@test.com",
                "password":"pass123",
            }
        }
