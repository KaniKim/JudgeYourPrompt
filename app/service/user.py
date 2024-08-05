from typing import AsyncGenerator, List

from fastapi import Depends
from passlib.context import CryptContext
from sqlalchemy.ext.asyncio import AsyncSession

from session.manager import get_db
from session.transactional import transactional
from repository.user import UserRepository
from schema.user import User, UserCreate, UserUpdate


class UserService:
    def __init__(self, user_repository: UserRepository):
        self._user_repo = user_repository
        self._pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

    @transactional
    async def get_user(self, user_id: int) -> User | List[User] | None:
        return await self._user_repo.get_user_by_id(user_id=user_id)

    @transactional
    async def update_user(self, user_id: int, user: UserUpdate) -> User | None:
        if await self._user_repo.check_user_by_id(user_id=user_id):
            await self._user_repo.update_user_by_id(user_id=user_id, user=user)
            return await self._user_repo.get_user_by_id(user_id=user_id)
        return None

    @transactional
    async def delete_user(self, user_id: int) -> bool:
        if await self._user_repo.check_user_by_id(user_id=user_id):
            return await self._user_repo.delete_user_by_id(user_id=user_id)
        return False

    @transactional
    async def create_user(self, user: UserCreate) -> None:
        user.password = self._pwd_context.hash(user.password)
        await self._user_repo.create_user(user)
