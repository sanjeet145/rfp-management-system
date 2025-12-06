from entity.models import Users,Vendors
from config.db import db
from entity.schemas import userSchema
from flask import jsonify
from utils.save_to_db import save_to_user, save_to_vendor
from utils.get_from_db import get_user_email
from flask_jwt_extended import create_access_token,decode_token
import datetime

def register_vendor(*args,**kwargs):
    try:
        res = save_to_vendor(**kwargs)
        if res["status"] == 201:
            return jsonify({"message":"vendor registered successfully"}),res["status"]
        else:
            return jsonify({"message":res["message"]}),res["status"]
    except Exception as e:
        return jsonify({"message":"something went wrong"},status=500)
    
def register_user(*args, **kwargs):
    try:
        res = save_to_user(**kwargs)
        if res["status"] == 201:
            return jsonify({"message":"user registered successfully"}),res["status"]
        else:
            return jsonify({"message":res["message"]}),res["status"]
    except Exception as e:
        return jsonify({"message":"something went wrong"}),500
    

def login_user(*args, **kwargs):
    try:
        email =kwargs.get("email")
        res = get_user_email(email)
        if res.get("email")==email:
            token = create_access_token(identity=res["id"], additional_claims=res, expires_delta=datetime.timedelta(hours=10))
            return jsonify({"message":token}),200
        return jsonify({"message":"Invalid email"}),401
    except Exception as e:
        return jsonify({"message":"something went wrong"}),500

    
