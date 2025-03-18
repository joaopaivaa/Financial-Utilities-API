from fastapi import FastAPI

app = FastAPI(title='Inflation Rate Adjust API',
              version='0.0.1')

@app.get("/brl_inflation_adjust")
def brl_inflation_adjust(data:Request):

  
    return {"message": "Olá, FastAPI!"}
