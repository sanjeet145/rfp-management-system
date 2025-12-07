from utils.prompts import USER_TO_JSON
from utils.get_llm_response import get_llm_repsonse
from config.db import db
from entity.models import RFPs, RFP_Items
from utils.exception_handler import ExceptionHandler
from entity.schemas import rfpSchema, rfpItemSchema
import sys
from utils.enums import rfp_status
from flask import jsonify
import json
import re

def save_rfp(input, user_id):
    try:
        text = get_llm_repsonse(prompt=USER_TO_JSON,input=input)
        text = re.sub(r'(\w+)\s*:', r'"\1":', text)
        text = re.sub(r':\s*([A-Za-z][A-Za-z0-9\s\-]*)(?=[,\}])', r': "\1"', text)
        response = json.loads(text)
        category = str(response.get("category")).lower()
        rfp = rfpSchema.load({
            "user_id": user_id,
            "description_raw": input,
            "item_category": category,
            "total_budget": response.get("total_budget"),
            "delivery_days": response["delivery_days"],
            "payment_terms": response["payment_terms"],
            "warranty_min_years": str(response["warranty_min_years"]),
            "status": rfp_status.ACTIVE
        })
        rfp = RFPs(**rfp)
        db.session.add(rfp)
        db.session.flush()
        items_to_add = []
        for item in response["items"]:
            item["rfp_id"] = rfp.id
            dumped = rfpItemSchema.dump(item)
            items_to_add.append(RFP_Items(**dumped))
        db.session.add_all(items_to_add)
        db.session.commit()
        return jsonify({"message":"RFP has been saved","category":category,"rfp_id":rfp.id}),201
    except Exception as e:
        raise ExceptionHandler(e, sys)