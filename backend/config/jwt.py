from flask_jwt_extended import JWTManager, decode_token
from flask import jsonify

jwt = JWTManager()

@jwt.expired_token_loader
def expired_token(*args, **kwargs):
    return jsonify({"message":"JWT expired please log in again"}),401

@jwt.invalid_token_loader
def invalid_token(error):
    return jsonify({"message":"Invalid token please log in again"}),401


def decoded_token(token):
    return decode_token(token)