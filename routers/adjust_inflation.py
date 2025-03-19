from fastapi import APIRouter
from base_model import AdjustInflationRequest
from adjust_inflation_functions import adjust_inflation

router = APIRouter()

@router.post("/adjust_inflation")
def adjust_inflation_route(data: AdjustInflationRequest):

    dates = data.dates
    values = data.values
    currency = data.currency
    present_date = data.present_date

    df = adjust_inflation(dates, values, currency, present_date)

    return df