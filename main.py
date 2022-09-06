import os
from typing import Union
from fastapi import FastAPI
from dotenv import load_dotenv
from fastapi.middleware.cors import CORSMiddleware
import motor.motor_asyncio

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

from src.controllers import health_controller, users_controller