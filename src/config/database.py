import os
import motor.motor_asyncio

mongodburl = os.environ.get("DB_CONNECTION_STRING")

client = motor.motor_asyncio.AsyncIOMotorClient(mongodburl)
environment = os.getenv("ENV", "dev")
if environment == "dev":
    db = client.chat_api
if environment == "test":
    db = client.test_db