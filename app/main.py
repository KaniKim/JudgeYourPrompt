from fastapi import FastAPI

from api.v1.dependencies.request import SessionMiddleware
from api import api_router


app = FastAPI()
app.include_router(api_router)
app.add_middleware(SessionMiddleware)
