from fastapi import FastAPI
import uvicorn
import end_points

app = FastAPI(title='Inflation Rate Adjust API',
              version='0.0.1')

app.include_router(end_points.router, tags=['Recipe Finder'])

if __name__ == "__main__":
    uvicorn.run('main:app', host="127.0.0.1", port=8000)
