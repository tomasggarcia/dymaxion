from fastapi import FastAPI
from dotenv import load_dotenv
from fastapi.middleware.cors import CORSMiddleware

load_dotenv(".env")

app = FastAPI(title='Chat Challenge', description='API for manage users and chat rooms')

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


from src.config import database
from src.controllers import health_controller, users_controller, friends_controller, chat_controller