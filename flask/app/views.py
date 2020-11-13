from app import app

@app.route("/")
def index():
    return "Hello from Flask.... You have successfully run a containerized Python-Flask app.... @Mohibullah Kamal"