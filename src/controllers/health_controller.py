from main import app

@app.get("/")
def health_status():
    return {"status": "ok"}