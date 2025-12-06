import logging
import os

file_path ='./logs/app.log'
os.makedirs(os.path.dirname(file_path), exist_ok=True)
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(lineno)d - %(filename)s - %(levelname)s - %(message)s" ,
    datefmt="%d-%m-%y %H:%M:%S",
    handlers=[
        logging.FileHandler(file_path),
        logging.StreamHandler()
    ]
)