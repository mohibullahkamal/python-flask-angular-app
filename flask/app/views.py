# from app import app
#
# @app.route("/")
# def index():
#     return "Hello from Flask.... You have successfully run a containerized Python-Flask app.... @Mohibullah Kamal"
#

from app import app
import os

@app.route("/")
def index():

    # Use os.getenv("key") to get environment variables
    app_name = os.getenv("APP_NAME")

    if app_name:
        return f"Hello from {app_name} running in a Docker container behind Nginx!.....@Mohibullah Kamal"

    return "Hello from Flask.....@Mohibullah Kamal"




# from app import app
# import os

# @app.route("/")
# def index():

#     # Use os.getenv("key") to get environment variables
#     app_name = os.getenv("APP_NAME")

#     if app_name:
#         return f"Hello from {app_name} running in a Docker container behind Nginx!.....@Mohibullah Kamal"

#     return "Hello from Flask.....@Mohibullah Kamal"
