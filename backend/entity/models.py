from config.db import db
import uuid

class Users(db.Model):
    __tablename__='users'
    id=db.Column(db.String(), primary_key=True, default=lambda: str(uuid.uuid4()))
    name = db.Column(db.String(), nullable = False)
    email = db.Column(db.String(), nullable = False, unique=True)
    phone = db.Column(db.String(), nullable = False)
    
class Vendors(db.Model):
    __tablename__='vendors'
    id = db.Column(db.String(), primary_key=True, default=lambda: str(uuid.uuid4()))
    name = db.Column(db.String(), nullable = False)
    company_name = db.Column(db.String(), nullable = False)
    item_category = db.Column(db.String(), nullable = False)
    address = db.Column(db.String(), nullable = False)
    phone = db.Column(db.Integer, nullable = False)
    email = db.Column(db.String(), nullable = False)

class RFPs(db.Model):
    __tablename__='rfps'
    id = db.Column(db.String(), primary_key=True, default=lambda: str(uuid.uuid4()))
    user_id = db.Column(db.String(), db.ForeignKey('users.id'), nullable=False)
    description_raw = db.Column(db.String(), nullable = False)
    item_category = db.Column(db.String(), nullable = False)
    total_budget = db.Column(db.Integer, nullable = False)
    delivery_days = db.Column(db.Integer, nullable = False)
    payment_terms = db.Column(db.String(), nullable = False)
    warranty_min_years = db.Column(db.String(), nullable = False)
    status = db.Column(db.String(), nullable = False)

class RFP_Items(db.Model):
    __tablename__='rfpItems'
    id = db.Column(db.String(), primary_key=True, default=lambda: str(uuid.uuid4()))
    rfp_id = db.Column(db.String(), db.ForeignKey('users.id'), nullable=False)
    name = db.Column(db.String(), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    specifications = db.Column(db.String(), nullable=False)

class Proposals(db.Model):
    __tablename__= 'proposals'
    id = db.Column(db.String(), primary_key=True, default=lambda: str(uuid.uuid4()))
    rfp_id = db.Column(db.String(), db.ForeignKey('users.id'), nullable=False)
    vendor_id = db.Column(db.String(), db.ForeignKey('vendors.id'), nullable=False)
    received_on = db.Column(db.String(), nullable=False)
    summary_ai = db.Column(db.String(), nullable=True, default="")
    summary_score = db.Column(db.Float(), nullable=True, default=0)

class Proposal_responses(db.Model):
    __tablename__='propsalResponses'
    id = db.Column(db.String(), primary_key=True, default=lambda: str(uuid.uuid4()))
    proposal_id = db.Column(db.String(), db.ForeignKey('proposals.id'), nullable=False)
    vendor_total_price = db.Column(db.String())
    vendor_delivery_days = db.Column(db.String())
    vendor_warranty_years = db.Column(db.String())
    notes = db.Column(db.String())

class Proposal_responses_items(db.Model):
    __tablename__='propsalResponsesItems'
    id = db.Column(db.String(), primary_key=True, default=lambda: str(uuid.uuid4()))
    propsalResponses_id = db.Column(db.String(), db.ForeignKey('propsalResponses.id'), nullable=False)
    item_name = db.Column(db.String(), nullable=False)
    unit_price = db.Column(db.String())
    total_price = db.Column(db.String())

class Email_message(db.Model):
    __tablename__='vendormail'
    id = db.Column(db.String(), primary_key=True)
    sender = db.Column(db.String(), primary_key=True)


