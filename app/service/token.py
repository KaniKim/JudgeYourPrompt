import datetime
import os
from fastapi.security import OAuth2PasswordBearer
import jwt

from fastapi import HTTPException
from starlette import status
from passlib.context import CryptContext

from model.user import User as UserModel
from service.base import BaseService
from schema.user import UserReturn
from repository.utils import exception_log
from session.transactional import transactional
from repository.user import UserRepository

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


class TokenService(BaseService[UserModel]):
    def __init__(self, user_repository: UserRepository):
        super().__init__(model=UserModel, repository=user_repository)
        self._user_repo = user_repository
        self._pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
        self.SECRET_KEY = os.getenv("SECRET_KEY")
        self.ALGORITHM = os.getenv("ALGORITHM")

    def _create_token(self, data: dict, expires_delta: int | None) -> str:
        to_encode = data.copy()

        if expires_delta:
            expire = datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(
                minutes=expires_delta
            )
        else:
            expire = datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(
                days=14
            )

        to_encode.update({"exp": expire})
        encoded_jwt = jwt.encode(to_encode, self.SECRET_KEY, algorithm=self.ALGORITHM)
        return encoded_jwt

    async def _verify_password(self, plain_password, hashed_password):
        return self._pwd_context.verify(plain_password, hashed_password)

    async def authenticate_user(self, email: str, password: str) -> bool:
        user = await self._user_repo.get_user_password(email=email)

        if not user:
            return False

        if not self._verify_password(
            plain_password=password, hashed_password=user.password
        ):
            return False

        return True

    async def create_refresh_token(self, data: dict) -> str:
        return self._create_token(data=data, expires_delta=14)

    async def create_access_token(
        self, data: dict, expires_delta: int | None = None
    ) -> str:
        return self._create_token(data=data, expires_delta=expires_delta)
