from ctypes import Union
import datetime
import os
import jwt

from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from pydantic import ValidationError
from schema.security import TokenPayload
from schema.user import UserReturn
from service.token import TokenService
from repository.user import UserRepository
from service.user import UserService
from session.manager import get_db

reuseable_oauth = OAuth2PasswordBearer(tokenUrl="/login", scheme_name="JWT")


class UserFactory:
    """
    This is the factory container that will instantiate all the controllers and
    repositories which can be accessed by the rest of the application.
    """

    JWT_SECRET_KEY = os.environ.get("SECRET_KEY")
    ALGORITHM = os.environ.get("ALGORITHM")
    user_repository = UserRepository

    def get_user_service(self, db_session=Depends(get_db)):
        return UserService(user_repository=self.user_repository(db=db_session))

    def get_token_service(self, db_sesion=Depends(get_db)):
        return TokenService(user_repository=self.user_repository(db=db_sesion))

    async def get_current_user(
        self, token: str = Depends(reuseable_oauth), db_sesion=Depends(get_db)
    ) -> UserReturn:
        user_repository = self.user_repository(db=db_sesion)
        try:
            if self.ALGORITHM is None:
                raise ValueError("ALGORITHM environment variable is not set.")
            payload = jwt.decode(
                token, self.JWT_SECRET_KEY, algorithms=[self.ALGORITHM]
            )
            if (
                datetime.datetime.fromtimestamp(payload.get("exp"))
                < datetime.datetime.now()
            ):
                raise HTTPException(
                    status_code=status.HTTP_401_UNAUTHORIZED,
                    detail="Token expired",
                    headers={"WWW-Authenticate": "Bearer"},
                )
        except (jwt.PyJWTError, ValidationError):
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Could not validate credentials",
                headers={"WWW-Authenticate": "Bearer"},
            )

        user = await user_repository.get_user_by_email(payload.get("email"))
        if user is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Could not find user",
            )
        return user
