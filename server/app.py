import uvicorn
from fastapi import FastAPI
from uvicorn import run

app = FastAPI()

if __name__ == '__main__':
    uvicorn.run(app)