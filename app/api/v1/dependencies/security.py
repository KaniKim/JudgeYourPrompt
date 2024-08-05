import os
import jwt
from typing import Annotated

from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status
from starlette.exceptions import HTTPException
from jwt.exceptions import InvalidTokenError

from session.manager import get_db
from model.user import User as UserModel
from repository.utils import exception_log
from session.transactional import transactional
from schema.user import User


SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM")


@transactional
@exception_log
async def get_current_user(
    token: Annotated[str, Depends(OAuth2PasswordBearer(tokenUrl="token"))],
) -> User:
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM or "HSA256"])
        email: str = payload.get("sub")
        query = await db.execute(select(UserModel).where(UserModel.email == email))
        user = query.scalar_one_or_none()
        if user is None:
            raise credentials_exception
        return User.model_validate(user)
    except InvalidTokenError:
        raise credentials_exception
