from app import app

@app.router("/")
def index():
    return "Hello from Flask...."