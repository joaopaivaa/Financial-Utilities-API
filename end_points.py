from fastapi import APIRouter
from base_model import InflationRequest, CurrencyConversionRequest
from adjust_inflation_functions import adjust_BRL_inflation
from currency_conversion import currency_conversion

router = APIRouter()

@router.post("/brl_inflation_adjust")
def brl_inflation_adjust(data: InflationRequest):

    dates = data.dates
    values = data.values
    present_date = data.present_date

    df = adjust_BRL_inflation(dates, values, present_date)

    return df

@router.post("/currency_conversion")
def currency_conversion(data: CurrencyConversionRequest):

    dates = data.dates
    values = data.values
    original_currency = data.original_currency

    df = currency_conversion(dates, values, original_currency)

    return df
