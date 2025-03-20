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

class AmortizationRequest(BaseModel):
    principal : float = Field(description='Principal', default=None)
    rate: float = Field(description='Rate', default=None)
    periods: int = Field(description='Time Periods', default=None)

class InterestRequest(BaseModel):
    amount: float = Field(description='Total Amount', default=None)
    principal: float = Field(description='Principal', default=None)
    rate: float = Field(description='Interest Rate', default=None)
    time: int = Field(description='Time Periods', default=None)
