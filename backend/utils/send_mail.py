from dotenv import load_dotenv
from config.logger import logging
from utils.exception_handler import ExceptionHandler
import requests
import sys
import os

load_dotenv()

def send_mail(from_user, to, subject,message):
	try:
		auth = os.getenv('MAIL_API_KEY')
		if auth is None:
			logging.error("mailing auth key is not found")
			return {"message":"error"}
		return requests.post(
			os.getenv("MAIL_URL"),
			auth=("api", auth),
			data={"from": from_user,
				"to": to,
				"subject": subject,
				"text": message})
	except Exception as e:
		raise ExceptionHandler(e,sys)