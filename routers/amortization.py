from fastapi import APIRouter
from base_model import AmortizationRequest
from amortization_functions import french_amortization, sac_amortization

router = APIRouter()

@router.post("/french_amortization")
def french_amortization_route(data: AmortizationRequest):

    principal = data.principal
    rate = data.rate
    periods = data.periods

    df = french_amortization(principal, rate, periods)

    return df

@router.post("/sac_amortization")
def sac_amortization_route(data: AmortizationRequest):

    principal = data.principal
    rate = data.rate
    periods = data.periods

    df = sac_amortization(principal, rate, periods)

    return df
