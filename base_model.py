from pydantic import BaseModel, Field

class IngredientsRequest(BaseModel):
    dates: str = Field(description='Dates', default=None)
    values: float = Field(description='Values', default=None)
    present_date: str = Field(description='Present Date', default=None)
