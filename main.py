from fastapi import FastAPI
import uvicorn
from routers import inflation_adjustment, currency_rate_conversion, interest, amortization

app = FastAPI(title='Financial Utilities API',
              version='0.0.1')

app.include_router(inflation_adjustment.router, tags=['Adjust Inflation Route'])
app.include_router(currency_rate_conversion.router, tags=['Currency Rate Conversion Route'])
app.include_router(interest.router, tags=['Simple and Compound Interest Calculation Route'])
app.include_router(amortization.router, tags=['French and SAC Amortization Calculation Route'])

if __name__ == "__main__":
    uvicorn.run('main:app', host="127.0.0.1", port=8000)
