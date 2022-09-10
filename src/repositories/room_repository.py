from typing import List
from src.config.database import db

class RoomRepository():
    friends_db = db["room"]

    async def create(self, participants: List[str]):
        room = await self.friends_db.insert_one({'participants': participants})
        return str(room.inserted_id)