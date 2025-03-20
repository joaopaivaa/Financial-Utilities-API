from fastapi import APIRouter
from base_model import InterestRequest
from interest_functions import simple_interest, compound_interest

router = APIRouter()

@router.post("/simple_interest")
def simple_interest_route(data: InterestRequest):

    amount = data.amount
    principal = data.principal
    rate = data.rate
    time = data.time

    missing_value = simple_interest(amount, principal, rate, time)

    return missing_value

@router.post("/compound_interest")
def compound_interest_route(data: InterestRequest):

    amount = data.amount
    principal = data.principal
    rate = data.rate
    time = data.time

    missing_value = compound_interest(amount, principal, rate, time)

    return missing_value
