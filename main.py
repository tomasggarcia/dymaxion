import os
from typing import Union
from fastapi import FastAPI
from dotenv import load_dotenv
import motor.motor_asyncio
from fastapi.middleware.cors import CORSMiddleware

load_dotenv(".env")

app = FastAPI(title='Chat Challenge', description='API for manage users and chat rooms')

mongodburl = os.environ.get("DB_CONNECTION_STRING")
client = motor.motor_asyncio.AsyncIOMotorClient(mongodburl)
db = client.user_ms

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}