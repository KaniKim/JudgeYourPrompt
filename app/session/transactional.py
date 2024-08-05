import functools

from contextvars import ContextVar
import logging
from typing import Any, Awaitable, Callable, Optional
import uuid
from sqlalchemy.ext.asyncio import AsyncSession

from .manager import session

db_session_context: ContextVar[Optional[AsyncSession]] = ContextVar(
    "db_session", default=None
)
AsyncCallable = Callable[..., Awaitable]


def transactional(func: AsyncCallable) -> AsyncCallable:
    @functools.wraps(func)
    async def _wrapper(*args, **kwargs):
        try:
            result = await func(*args, **kwargs)
            logging.info(await session.commit())
        except Exception as e:
            logging.info(await session.rollback())
            raise e
        finally:
            logging.info(await session.close())
        return result

    return _wrapper
