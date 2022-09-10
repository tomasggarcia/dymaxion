from typing import List
from pydantic import BaseModel

class Room(BaseModel):
    participants: List[str] = []

    class Config:
        schema_extra = {
            "example": {
                "participants":["email@test.com", "emaild@test.com"]
            }
        }