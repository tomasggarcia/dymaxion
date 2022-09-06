from pydantic import BaseModel, Field

class UserModel(BaseModel):
    username: str
    email: str
    password: str