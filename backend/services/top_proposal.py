from utils.get_from_db import get_vendor_id, get_top_proposal_rfp_id, get_proposal_response_proposal_id

def top_proposal(rfp_id):
    proposal = get_top_proposal_rfp_id(rfp_id)
    vendor = get_vendor_id(proposal.get("vendor_id"))
    proposal_responses = get_proposal_response_proposal_id(proposal.get("id"))
    return {
        "proposal":proposal,
        "vendor":vendor,
        "proposal_responses":proposal_responses
    }