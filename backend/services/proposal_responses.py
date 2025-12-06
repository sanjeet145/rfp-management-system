from utils.get_from_db import get_proposal_and_response_proposal_id

def proposal_responses(page:int, per_page:int,rfp_id:str):
    return get_proposal_and_response_proposal_id(page, per_page, rfp_id)