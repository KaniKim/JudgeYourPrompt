from typing import Awaitable, Callable
import uuid
from fastapi import Request, Response
from fastapi import status as HTTPstatus
from starlette.middleware.base import BaseHTTPMiddleware

from session.manager import reset_session_context, set_session_context, session

__all__ = ["SessionMiddleware"]


class SessionMiddleware(BaseHTTPMiddleware):
    async def dispatch(
        self, request: Request, call_next: Callable[[Request], Awaitable[Response]]
    ) -> Response:
        response = Response(
            "Internal server error",
            status_code=HTTPstatus.HTTP_500_INTERNAL_SERVER_ERROR,
        )
        session_id = hash(uuid.uuid4())
        context = set_session_context(session_id=session_id)
        try:
            response = await call_next(request)
        except Exception as e:
            raise e
        finally:
            await session.remove()
            reset_session_context(context=context)

        return response
