from flask import Blueprint, request,jsonify
from services.authentication import register_vendor, register_user
from services.save_rfp import save_rfp
from utils.get_from_db import get_vendor_category,get_all_rfp,get_rfp_id
from flask_jwt_extended import jwt_required
from services.authentication import login_user
from config.jwt import decoded_token
from services.send_rfp_proposal import send_rfp_proposal
from services.vendor_response import vendor_response
from config.logger import logging
from services.top_proposal import top_proposal
from services.proposal_responses import proposal_responses
from entity.models import Email_message
from entity.schemas import emailSchema
from config.db import db
import re
import asyncio
# from concurrent.futures import ThreadPoolExecutor
# background_executor = ThreadPoolExecutor(max_workers=5)

router=Blueprint("routes",import_name=__name__)

@router.post('/register')
def register():
    # call the register-vendor function if its vendor register else register the user
    data = request.get_json()
    if data['is_vendor']:
        return register_vendor(**data)
    else:
        return register_user(**data)

@router.post('/login')
def login():
    data = request.get_json()
    return login_user(**data)

@router.post('/save-rfp')
@jwt_required()
def save_rfps():
    data = request.get_json()
    user_id = decoded_token(request.headers.get("Authorization")[7:]).get("sub")
    return save_rfp(data["query"],user_id)

@router.get('/get-rfps')
def rfps():
    userid = decoded_token(request.headers.get("Authorization")[7:]).get("sub")
    return jsonify({"message":get_all_rfp(userid)})

@router.get('/get-rfp')
def single_rfps():
    rfp_id = request.headers.get("Rfpid")
    return jsonify({"message":get_rfp_id(rfp_id)})

@router.get('/get-vendors')
def show_vendors():
    # get the user description and return the paginated vendors
    category = request.args.get("category","electronics")
    page = int(request.args.get("page",1))
    per_page = int(request.args.get("perpage",10))
    return jsonify({"message":get_vendor_category(page,per_page,category)}),200

@router.post('/send-proposal')
@jwt_required()
def send_proposal():
    data = request.get_json()
    return send_rfp_proposal(data.get("rfpid"), data.get("vendorid"))

@router.post('/vendor-response')
def vendor_reponses():
    logging.warning("got proposal response.......")
    sender = request.form.get("from")
    # messageid = request.form.get("Message-Id").split("<")[-1].split(">")[0]
    subject = request.form.get("subject")
    body_html = request.form.get("stripped-html")
    body_text = request.form.get("stripped-text")
    to_address = request.form.get("To")
    messageid = re.search(r'<([a-f0-9\-]+)@', to_address).group(1)
    if (db.session.query(Email_message).filter(Email_message.id ==messageid).first()):
        logging.info(f"got response for same proposal {messageid}")
        return jsonify({"message":"ok"}),200
    regex = r'<(.+?)>' 
    match = re.search(regex, sender)
    data = emailSchema.load({"id":messageid,"sender":match.group(1)})
    email = Email_message(**data)
    db.session.add(email)
    db.session.commit()

    attachments_data = []

    for key, file in request.files.items():
        raw_bytes = file.read()
        attachments_data.append({
            "filename": file.filename,
            "mime_type": file.content_type,
            "size_bytes": len(raw_bytes),
            "raw_bytes": raw_bytes,
        })

    vendor_packet = {
        "sender": sender,
        "subject": subject,
        "body_html": body_html,
        "body_text": body_text,
        "to": to_address,
        "attachments": attachments_data,
    }
    # asyncio.create_task(vendor_response(vendor_packet))
    # background_executor.submit(
    #     asyncio.run,
    #      
    # )
    return vendor_response(vendor_packet)

@router.get('/proposal-response')
def proposal_response():
    rfp_id = request.headers.get("Rfpid")
    page = int(request.args.get("page",1))
    per_page = int(request.args.get("perpage",10))
    return jsonify({"message":proposal_responses(page, per_page, rfp_id)}),200

@router.get('/best-proposal')
def best_proposal():
    rfp_id = request.headers.get("Rfpid")
    return jsonify({"message":top_proposal(rfp_id)}),200