import os
from main import app
from typing import List
from fastapi import WebSocket, WebSocketDisconnect, Response, Request, status
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.templating import Jinja2Templates
from fastapi.encoders import jsonable_encoder
from src.services.room_service import RoomService
from src.services.users_service import UserService

root = os.path.dirname(os.path.abspath(__file__))
templates = Jinja2Templates(directory="src/templates")
user_service = UserService()
backend_url = os.getenv("BACKEND_URL")

class ConnectionManager:
    def __init__(self):
        self.active_connections: List[WebSocket] = []

    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        self.active_connections.append(websocket)

    def disconnect(self, websocket: WebSocket):
        self.active_connections.remove(websocket)

    async def send_personal_message(self, message: str, websocket: WebSocket):
        await websocket.send_text(message)

    async def broadcast(self, message: str):
        for connection in self.active_connections:
            await connection.send_text(message)

manager = ConnectionManager()


@app.get("/home/{email}", response_class=HTMLResponse)
async def read_item(request: Request, email: str):
    friend_list = await user_service.get_friend_list(email)
    return templates.TemplateResponse(
        "friends.html", {
            "request": request, 
            "email": email,
            "friends": friend_list,
            "backend_url": backend_url
            }
        )

@app.get("/chat/{room}", response_class=HTMLResponse)
async def chat_page(request: Request, email: str, room: str):
    room_service = RoomService()
    email_in_room = await room_service.validate_email_in_room(email, room)
    print(email_in_room) 
    if email_in_room is False:
        return templates.TemplateResponse("unauthorized.html", {"request": request})
    return templates.TemplateResponse(
        "chat.html", {
            "request": request, 
            "room": room,
            "email": email,
            "backend_url": backend_url
            }
        )

@app.websocket("/ws/{room}")
async def websocket_endpoint(websocket: WebSocket, room: str, email: str):
    await manager.connect(websocket)
    try: 
        while True:
            data = await websocket.receive_text()
            await manager.broadcast(f"{email}: {data}")
    except WebSocketDisconnect:
        manager.disconnect(websocket)
        await manager.broadcast(f"Client #{email} left the chat")

@app.post("/new-room")
async def new_room(participants: List[str]):
    room_service = RoomService()
    room: str = await room_service.create_chat_room(participants)
    return JSONResponse(status_code=status.HTTP_201_CREATED, content=jsonable_encoder(room))
