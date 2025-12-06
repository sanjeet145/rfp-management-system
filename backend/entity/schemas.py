from marshmallow import Schema, fields

class UserSchema(Schema):
    id= fields.Str(dump_only=True)
    name = fields.Str(required=True)
    email = fields.Str(required=True)
    phone = fields.Str(required=True)
    
class VendorSchema(Schema):
    id= fields.Str(dump_only=True)
    name = fields.Str(required=True)
    company_name = fields.Str(required=True)
    item_category = fields.Str(required=True)
    address = fields.Str(required=True)
    email = fields.Str(required=True)
    phone = fields.Str(required=True)

class RfpSchema(Schema):
    id= fields.Str(dump_only=True)
    user_id = fields.Str(required=True)
    description_raw = fields.Str(required=True)
    item_category = fields.Str(required=True)
    total_budget = fields.Str(required=True)
    delivery_days = fields.Str(required=True)
    payment_terms = fields.Str(required=True)
    warranty_min_years = fields.Str(required=True)
    status = fields.Str(required=True)

class RfpItemSchema(Schema):
    id= fields.Str(dump_only=True)
    rfp_id = fields.Str(required=True)
    name = fields.Str(required=True)
    quantity = fields.Int(required=True)
    specifications = fields.Str(required=True)

class ProposalsSchema(Schema):
    id= fields.Str(dump_only=True)
    rfp_id = fields.Str(required=True)
    vendor_id = fields.Str(required=True)
    received_on = fields.Str(required=True)
    summary_ai = fields.Str(required=False)
    summary_score = fields.Float(required=False)

class ProposalResponsesSchema(Schema):
    id= fields.Str(dump_only=True)
    proposal_id = fields.Str(required=True)
    vendor_total_price = fields.Str(required=True)
    vendor_delivery_days = fields.Str(required=True)
    vendor_warranty_years = fields.Str(required=True)
    notes = fields.Str(required=True)

class ResponsesItemsSchema(Schema):
    id= fields.Str(dump_only=True)
    propsalResponses_id = fields.Str(required=True)
    item_name = fields.Str(required=True)
    unit_price = fields.Str(required=True)
    total_price = fields.Str(required=True)

class EmailSchema(Schema):
    id=fields.Str()
    sender = fields.Str()

emailSchema = EmailSchema()
userSchema= UserSchema()
vendorSchema = VendorSchema()
rfpSchema = RfpSchema()
rfpItemSchema = RfpItemSchema()
proposalsSchema = ProposalsSchema()
proposalResponsesSchema= ProposalResponsesSchema()
responsesItemsSchema = ResponsesItemsSchema()