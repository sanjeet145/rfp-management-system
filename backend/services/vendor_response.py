from utils.get_from_db import get_rfp_id,get_rfp_items_rfp_id,get_proposal_response_proposal_id, get_proposals_proposal_id
from flask import jsonify
from utils.get_llm_response import get_llm_repsonse, get_llm_response_with_attachments
from utils.prompts import SUMMARIZE_PROPOSAL_RESPONSE, VENDOR_TO_JSON
from config.db import db
from entity.models import Proposal_responses, Proposal_responses_items, Proposals
from entity.schemas import proposalResponsesSchema, responsesItemsSchema
from utils.exception_handler import ExceptionHandler
import re
import json
import sys
from config.logger import logging


def save_proposal_summary(proposal_id, vendor_res):
    try:
        proposalResponse = proposalResponsesSchema.load({
            "proposal_id":proposal_id,
            "vendor_total_price":str(vendor_res.get("total_cost")),
            "vendor_delivery_days":str(vendor_res.get("delivery_days")),
            "vendor_warranty_years":str(vendor_res.get("warranty_min_years")),
            "notes":vendor_res.get("additional_note")
        })
        proposalResponse = Proposal_responses(**proposalResponse)
        db.session.add(proposalResponse)
        db.session.flush()
        items_to_add = []
        for item in vendor_res["items"]:
            item["propsalResponses_id"] = proposalResponse.id
            dumped = responsesItemsSchema.dump(item)
            items_to_add.append(Proposal_responses_items(**dumped))
        db.session.add_all(items_to_add)
        db.session.commit()
        logging.info("saved the vendor response")
        return "saved successfully"
    except Exception as e:
        raise ExceptionHandler(e, sys)

def update_and_save_proposal_summary(proposal_id, vendor_res):
    try:
        proposal = db.session.query(Proposals).filter(Proposals.id == proposal_id).first()
        if not proposal:
            raise Exception(f"Proposal with ID {proposal_id} not found")
        rfp_id = proposal.rfp_id
        user_proposal = get_rfp_id(rfp_id)
        user_proposal["items"]=get_rfp_items_rfp_id(rfp_id)
        query=f'''' give me the score and summary of comparing the \n\n\
            user requirements:\n\
                {user_proposal}\n\n\
            and vendor response"\n\
                {vendor_res}
            '''
        response = get_llm_repsonse(SUMMARIZE_PROPOSAL_RESPONSE,query)
        response= json.loads(response)
        proposal.summary_ai=response["summary_ai"]
        proposal.summary_score=float(response["summary_score"])
        save_proposal_summary(proposal_id, vendor_res)
        db.session.commit()
        return "saved successfully"
    except Exception as e:
        raise ExceptionHandler(e,sys)

def vendor_response(vendor_packet:dict):
    #  after receiving the vendor response always summarize and update the proposals table and save the response
    match = re.search(r'<([a-f0-9\-]+)@', vendor_packet['to'])
    # EMAIL TEXT:
    #     {vendor_packet['body_text']}
    # \n
    input_text = f'''
    EMAIL HTML:
        {vendor_packet['body_html']}
    '''
    if match:
        text = get_llm_response_with_attachments(VENDOR_TO_JSON,vendor_packet,input_text)
        # logging.info(f"text to decode {text}")
        # text = re.sub(r'(\w+)\s*:', r'"\1":', text)
        # text = re.sub(r':\s*([A-Za-z][A-Za-z0-9\s\-]*)(?=[,\}])', r': "\1"', text)
        response = json.loads(text)
        extracted_id = match.group(1)
        update_and_save_proposal_summary(extracted_id,response)
    return jsonify({"message":"response recievd from the vendor"}),200