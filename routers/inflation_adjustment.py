from fastapi import APIRouter
from base_model import AdjustInflationRequest
from inflation_adjustment_functions import inflation_adjustment

router = APIRouter()

@router.post("/inflation_adjustment")
def inflation_adjustment_route(data: AdjustInflationRequest):

    dates = data.dates
    values = data.values
    currency = data.currency
    present_date = data.present_date

    df = inflation_adjustment(dates, values, currency, present_date)

    return df