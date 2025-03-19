from fastapi import APIRouter
from base_model import CurrencyRateConversionRequest
from currency_rate_conversion_functions import currency_rate_conversion

router = APIRouter()

@router.post("/currency_rate_conversion")
def currency_rate_conversion_route(data: CurrencyRateConversionRequest):

    dates = data.dates
    values = data.values
    original_currency = data.original_currency

    df = currency_rate_conversion(dates, values, original_currency)

    return df