import os
from main import app
from typing import List
from fastapi import WebSocket, WebSocketDisconnect, Response, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from src.services.users_service import UserService


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


root = os.path.dirname(os.path.abspath(__file__))
manager = ConnectionManager()
templates = Jinja2Templates(directory="src/templates")
user_service = UserService()
backend_url = os.getenv("BACKEND_URL")

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

@app.get("/chat")
async def chat_page():
    with open(os.path.join(root, '../templates/chat.html')) as fh:
        data = fh.read()
    return Response(content=data, media_type="text/html")

@app.websocket("/ws/{email}")
async def websocket_endpoint(websocket: WebSocket, email: str):
    await manager.connect(websocket)
    try:
        while True:
            data = await websocket.receive_text()
            await manager.send_personal_message(f"You wrote: {data}", websocket)
            await manager.broadcast(f"Client #{email} says: {data}")
    except WebSocketDisconnect:
        manager.disconnect(websocket)
        await manager.broadcast(f"Client #{email} left the chat")