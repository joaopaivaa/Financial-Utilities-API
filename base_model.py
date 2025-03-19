from pydantic import BaseModel, Field

class AdjustInflationRequest(BaseModel):
    dates: list[str] = Field(description='Dates', default=None)
    values: list[float] = Field(description='Values', default=None)
    currency: str = Field(description='Values', default=None)
    present_date: str = Field(description='Present Date', default=None)

class CurrencyRateConversionRequest(BaseModel):
    dates: list[str] = Field(description='Dates', default=None)
    values: list[float] = Field(description='Values', default=None)
    original_currency: str = Field(description='Original Currency', default=None)
