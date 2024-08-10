from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from api.v1.dependencies.request import SessionMiddleware
from api import api_router


app = FastAPI()

origins = [
    "http://localhost:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(api_router)
app.add_middleware(SessionMiddleware)
