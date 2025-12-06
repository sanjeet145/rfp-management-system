from entity.models import Users,Vendors, RFP_Items, RFPs,Proposals, Proposal_responses
from config.db import db
from utils.exception_handler import  ExceptionHandler
from entity.schemas import userSchema,rfpSchema,vendorSchema
from utils.get_from_db import get_user_email,get_vendor_email
import sys
def save_to_RFP(*args,**kwargs):
    try:
        rfp = rfpSchema.dump(kwargs)
        rfp = RFPs(**kwargs)
        db.session.add(rfp)
        db.session.commit()
    except Exception as e:
        raise ExceptionHandler(e, sys)

def save_to_user(*args,**kwargs):
    try:
        temp = userSchema.dump(kwargs)
        user = Users(**temp)
        email = temp["email"]
        if len(get_user_email(email))>0:
            return {"message":f"user with {user.email} already exists", "status":205}
        db.session.add(user)
        db.session.commit()
        return {"message":user.id, "status":201}
    except Exception as e:
        raise ExceptionHandler(e, sys)
    
def save_to_vendor(*args,**kwargs):
    try:
        temp = vendorSchema.dump(kwargs)
        vendor = Vendors(**temp)
        if len(get_vendor_email(temp["email"]))>0:
            return {"message":f"user with {temp["email"]} already exists", "status":301}
        db.session.add(vendor)
        db.session.commit()
        return {"message":vendor.id, "status":201}
    except Exception as e:
        raise ExceptionHandler(e, sys)

def save_to_rfp_items(*args, **kwargs):
    try:
        item = RFP_Items(**kwargs)
        db.session.add(item)
        db.session.commit()
        return {"message":item.id, "status":201}
    except Exception as e:
        raise ExceptionHandler(e, sys)

def save_to_rfp_items_multiple(items:list[RFP_Items]):
    try:
        db.session.addall(items)
        db.session.commit()
        return {"message":"items saved successfully", "status":201}
    except Exception as e:
        raise ExceptionHandler(e, sys)
    

def save_to_proposals(*args, **kwargs):
    try:
        proposal = Proposals(**kwargs)
        db.session.add(proposal)
        db.session.commit()
        return {"message":proposal.id, "status":201}
    except Exception as e:
        raise ExceptionHandler(e, sys)