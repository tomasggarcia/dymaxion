from main import app
from fastapi.encoders import jsonable_encoder
from fastapi import status
from fastapi.responses import JSONResponse

@app.get("/")
def health_status():
   return JSONResponse(status_code=status.HTTP_200_OK, content=jsonable_encoder({"status": 'ok'}))