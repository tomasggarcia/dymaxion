import os
import motor.motor_asyncio

mongodburl = os.environ.get("DB_CONNECTION_STRING")

client = motor.motor_asyncio.AsyncIOMotorClient(mongodburl)
db = client.chat_api