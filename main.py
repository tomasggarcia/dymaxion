import os
from typing import Union
from fastapi import FastAPI

app = FastAPI(title='Chat Challenge', description='API for manage users and chat rooms')


@app.get("/")
def read_root():
    return {"Hello": "World"}
