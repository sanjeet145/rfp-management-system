from config.db import db
from utils.exception_handler import ExceptionHandler
from entity.models import Users, Vendors,RFPs,RFP_Items, Proposals, Proposal_responses, Proposal_responses_items
from entity.schemas import userSchema,vendorSchema,rfpSchema,rfpItemSchema, proposalsSchema, proposalResponsesSchema, responsesItemsSchema
import sys

def get_user_email(email):
    try:
        return userSchema.dump(db.session.query(Users).filter(Users.email == email).first())
    except Exception as e:
        raise ExceptionHandler(e, sys)
    
def get_vendor_email(email):
    try:
        return userSchema.dump(db.session.query(Vendors).filter(Vendors.email == email).first())
    except Exception as e:
        raise ExceptionHandler(e, sys)
    
def get_vendor_id(vendor_id):
    try:
        return vendorSchema.dump(db.session.query(Vendors).filter(Vendors.id == vendor_id).first())
    except Exception as e:
        raise ExceptionHandler(e, sys)

def get_vendor_category(page:int , per_page:int, category:str):
    try:
        # request.args.get("page", 1)
        query = db.session.query(Vendors).filter(str(Vendors.item_category).lower() == str(category).lower())
        vendors = query.offset((page - 1) * per_page).limit(per_page).all()
        total = query.count()
        return {
            "page": page,
            "per_page": per_page,
            "total": total,
            "items": vendorSchema.dump(vendors, many=True)
        }
    except Exception as e:
        raise ExceptionHandler(e, sys)

def get_all_rfp(userid):
    try:
        return rfpSchema.dump(db.session.query(RFPs).filter(RFPs.user_id == userid).all(),many=True)
    except Exception as e:
        raise ExceptionHandler(e, sys)
    
def get_rfp_id(rfp_id):
    try:
        rfp = rfpSchema.dump(db.session.query(RFPs).filter(RFPs.id == rfp_id).first())
        rfp["items"] = get_rfp_items_rfp_id(rfp_id)
        return rfp
    except Exception as e:
        raise ExceptionHandler(e, sys)
    
def get_rfp_items_rfp_id(rfp_id):
    try:
        return rfpItemSchema.dump(db.session.query(RFP_Items).filter(RFP_Items.rfp_id == rfp_id).all(),many=True)
    except Exception as e:
        raise ExceptionHandler(e, sys)
    
def get_proposals_rfp_id(rfp_id):
    try:
        return proposalsSchema.dump(db.session.query(Proposals).filter(Proposals.rfp_id == rfp_id).all(),many=True)
    except Exception as e:
        raise ExceptionHandler(e, sys)

def get_proposals_query_rfp_id(page:int , per_page:int, rfp_id:str):
    try:
        query = db.session.query(Proposals).filter(Proposals.rfp_id == rfp_id).order_by(Proposals.summary_score.desc())
        proposals = query.offset((page -1)*per_page).limit(per_page).all()
        total = query.count()
        proposals = proposalsSchema.dump(proposals, many=True)
        for proposal in proposals:
            proposal["vendor"]=get_vendor_id(proposal.get("vendor_id"))
        return {
            "page": page,
            "per_page": per_page,
            "total": total,
            "items": proposals
        }
    except Exception as e:
        raise ExceptionHandler(e, sys)
  
def get_top_proposal_rfp_id(rfp_id):
    try:
        return proposalsSchema.dump(db.session.query(Proposals).filter(Proposals.rfp_id == rfp_id).order_by(Proposals.summary_score.desc()).first())
    except Exception as e:
        raise ExceptionHandler(e, sys)

def get_proposals_proposal_id(proposal_id):
    try:
        return proposalsSchema.dump(db.session.query(Proposals).filter(Proposals.id == proposal_id).first())
    except Exception as e:
        raise ExceptionHandler(e, sys)

def get_proposal_response_proposal_id(proposal_id):
    try:
        responses = proposalResponsesSchema.dump(db.session.query(Proposal_responses).filter(Proposal_responses.proposal_id == proposal_id).all(),many=True)
        for response in responses:
            response["items"]= responsesItemsSchema.dump(db.session.query(Proposal_responses_items).filter(Proposal_responses_items.propsalResponses_id == response["id"]).all(),many=True)
        return responses
    except Exception as e:
        raise ExceptionHandler(e, sys)
    

def get_proposal_and_response_proposal_id(page:int , per_page:int, rfp_id:str):
    try:
        proposals = get_proposals_query_rfp_id(page,per_page,rfp_id).get("items")
        for proposal in proposals:
            proposal["response"]=get_proposal_response_proposal_id(proposal.get("id"))
        return proposals
    except Exception as e:
        raise ExceptionHandler(e, sys)