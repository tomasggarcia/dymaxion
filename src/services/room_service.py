from typing import List
from src.repositories.room_repository import RoomRepository


class RoomService():
    friend_repository = RoomRepository()
          
    async def create_chat_room(self, participants: List[str]):
         return await self.friend_repository.create(participants)