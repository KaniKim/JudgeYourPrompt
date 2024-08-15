import asyncio
import logging

from contextlib import asynccontextmanager
import sys
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from alembic.config import Config
from alembic import command
from sqlalchemy import create_engine

from api.v1.dependencies.request import SessionMiddleware
from api import api_router
from session.base_settings import settings


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
