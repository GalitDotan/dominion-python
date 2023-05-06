from uvicorn import run
from fastapi import FastAPI
from server.base import api_router as web_app_router, api_router


def include_router(app):
    app.include_router(api_router)
    app.include_router(web_app_router)


def start_application():
    app = FastAPI()
    include_router(app)
    return app


app = start_application()
run(app)
