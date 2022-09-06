from main import app
from src.services.users_service import UserService

@app.get("/users")
def health_status():
    user = UserService.create_user()
    return {"response": user}