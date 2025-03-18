from fastapi import APIRouter
from base_model import InflationRequest
from adjust_inflation_functions import adjust_BRL_inflation

router = APIRouter()

@router.post("/brl_inflation_adjust")
def brl_inflation_adjust(data: InflationRequest):

    dates = data.dates
    values = data.values
    present_date = data.present_date

    df = adjust_BRL_inflation(dates, values, present_date)

    return df
