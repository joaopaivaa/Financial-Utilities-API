from fastapi import FastAPI
import uvicorn
from routers import adjust_inflation, currency_rate_conversion

app = FastAPI(title='Financial Utilities API',
              version='0.0.1')

app.include_router(adjust_inflation.router, tags=['Adjust Inflation Route'])
app.include_router(currency_rate_conversion.router, tags=['Currency Rate Conversion Route'])

if __name__ == "__main__":
    uvicorn.run('main:app', host="127.0.0.1", port=8000)
