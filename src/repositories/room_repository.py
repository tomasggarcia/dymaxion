from typing import List
from src.models.rooms_model import Room
from src.config.database import db
from bson.objectid import ObjectId

class RoomRepository():
    friends_db = db["room"]

    async def create(self, participants: List[str]):
        room = await self.friends_db.insert_one({'participants': participants})
        return str(room.inserted_id)

    async def find_room_participants(self, room: str):
        print(room)
        room: Room = await self.friends_db.find_one({"_id": ObjectId(room)})
        return room['participants']