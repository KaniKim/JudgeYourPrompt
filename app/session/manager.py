import asyncio
import sys
from contextvars import ContextVar, Token
from typing import AsyncGenerator

from sqlalchemy import create_engine, text
from sqlalchemy.ext.asyncio import (
    AsyncSession,
    async_scoped_session,
    async_sessionmaker,
    create_async_engine,
)
from sqlalchemy.orm import Session, declarative_base, sessionmaker
from sqlalchemy.sql.expression import Delete, Insert, Update

from session.base_settings import settings, check_db

session_context: ContextVar[int] = ContextVar("session_context")


def get_session_context() -> int:
    return session_context.get()


def set_session_context(session_id: int) -> Token:
    return session_context.set(session_id)


def reset_session_context(context: Token) -> None:
    session_context.reset(context)


def wait_for_db(db_uri):
    """checks if database connection is established"""

    _local_engine = create_engine(db_uri)

    _LocalSessionLocal = sessionmaker(
        autocommit=False, autoflush=False, bind=_local_engine
    )

    try:
        # Try to create session to check if DB is awake
        db_session = _LocalSessionLocal()
        # try some basic query
        db_session.execute(text("SELECT 1"))
        db_session.commit()
    except Exception as err:
        print(f"Connection error: {err}")


wait_for_db(check_db)

engines = {
    "reader": create_async_engine(
        settings.database_url, pool_recycle=3600, pool_pre_ping=True
    ),
    "writer": create_async_engine(
        settings.database_url, pool_recycle=3600, pool_pre_ping=True
    ),
}


class RoutingSession(Session):
    def get_bind(self, mapper=None, clause=None, **kwargs):
        if self._flushing or isinstance(clause, (Update, Delete, Insert)):
            return engines["writer"].sync_engine
        return engines["reader"].sync_engine


async_session_factory = async_sessionmaker(
    class_=AsyncSession,
    sync_session_class=RoutingSession,
    expire_on_commit=False,
)

session = async_scoped_session(
    session_factory=async_session_factory,
    scopefunc=get_session_context,
)


async def get_db() -> AsyncGenerator[AsyncSession, None]:
    async with session() as db:
        try:
            yield db
        finally:
            await db.close()


Base = declarative_base()
