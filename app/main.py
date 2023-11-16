import uvicorn
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from api.api import router as api_router
from app.config import FastAPIConf
from app.core.config import PROJECT_NAME
from db.mongodb_utils import close_mongo_connection, connect_to_mongo

app = FastAPI(title=PROJECT_NAME)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.add_event_handler("startup", connect_to_mongo)
app.add_event_handler("shutdown", close_mongo_connection)

app.include_router(api_router)

# Running of app.
if __name__ == "__main__":
    uvicorn.run(app, host=FastAPIConf.HOST, port=FastAPIConf.PORT)
