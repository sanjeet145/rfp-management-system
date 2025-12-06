from flask import Flask
from config.db import db
from utils.exception_handler import ExceptionHandler
from config.logger import logging
from controller.routes import router
from utils.exception_handler import ExceptionHandler
import os
from dotenv import load_dotenv
from config.jwt import jwt
from flask_cors import CORS
# from concurrent.futures import ThreadPoolExecutor
# import asyncio
load_dotenv()

app = Flask(__name__)
CORS(app)
app.register_blueprint(router)
logging.info("App is running")

app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URI','sqlite:///testing.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config["JWT_SECRET_KEY"] = os.getenv("JWT_SECRET_KEY")
db.init_app(app)
jwt.init_app(app)
with app.app_context():
    logging.info(f"creating the tables")
    db.create_all()

@app.errorhandler(ExceptionHandler)
def handle_custom_exception(e):
    return e.to_response()

# background_executor = ThreadPoolExecutor(max_workers=5)
# def run_background_task_with_context(app, coroutine_func, *args, **kwargs):
#     """Executes an async task in a background thread with the Flask App Context."""
#     with app.app_context():
#         asyncio.run(coroutine_func(*args, **kwargs))

if __name__ == "__main__":
    app.run(debug=True, port=3000)
# input="I need to procure laptops and monitors for our new office. Budget is $50,000 total. Need delivery within 30 dyas. We need 20 laptops with 16GB RAM and 15 monitors 27-inch. Payment terms should be net 30, and We need at least 1 year warranty."