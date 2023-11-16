from fastapi import FastAPI
from uvicorn import run

from OLD.user import User

USERS = [User('siri'), User('alexa')]

app = FastAPI()


@app.get('/')
def root():
    return USERS


if __name__ == '__main__':
    run(app)
