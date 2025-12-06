from utils.send_mail import send_mail
from utils.save_to_db import save_to_proposals
from utils.get_from_db import get_vendor_id,get_rfp_id, get_rfp_items_rfp_id
from utils.prompts import VENDOR_EMAIL_MESSAGE
from utils.get_llm_response import get_llm_repsonse
from utils.exception_handler import ExceptionHandler
from flask import jsonify
import sys
import os
from dotenv import load_dotenv
import datetime
from config.logger import logging
load_dotenv()

SUBJECT = "Requesting for proposal"

def send_rfp_proposal(rfp_id, vendor_id):
    try:
        vendor = get_vendor_id(vendor_id)
        rfp = get_rfp_id(rfp_id)
        if len(vendor)>0 and vendor.get('email') and len(rfp)>0 and rfp.get("id"):
            items = get_rfp_items_rfp_id(rfp_id)
            proposal = {"rfp_id":rfp_id,"vendor_id":vendor_id,"received_on":datetime.datetime.now()}
            del rfp['user_id']
            del rfp['id']
            del rfp['description_raw']
            del rfp['status']
            proposal = save_to_proposals(**proposal)
            response = get_llm_repsonse(prompt= VENDOR_EMAIL_MESSAGE, input=f"user has requested this {vendor.get("name")} vendor for items {items} and the other details are {rfp}")
            from_user = f"proposal <{proposal.get("message")}@{os.getenv("MAIL_DOMAIN")}>"
            send_mail(from_user,vendor.get("email"),SUBJECT,response)
            logging.info("Mail is sent to the vendor")
            return jsonify({"message":"Email sent successfully"}),200
        return jsonify({"message":"Missing details failed to send the email"}),401
    except Exception as e:
        raise ExceptionHandler(e, sys)