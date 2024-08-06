from abc import ABC
import logging
from typing import List

from sqlalchemy import select, update, delete, exists
from sqlalchemy.ext.asyncio import AsyncSession

from repository.base import BaseRepository
from repository.utils import exception_log, repository_log
from schema.user import UserCreate, UserInternal, UserReturn, UserUpdate
from model.user import User as UserModel


class UserBaseRepository(ABC, BaseRepository[UserModel]):

    async def get_user_by_email(self, email: str):
        pass

    async def get_user_by_id(self, user_id: int):
        pass

    async def create_user(self, user: UserCreate):
        pass

    async def update_user_by_id(self, user_id: int, user: UserUpdate):
        pass

    async def delete_user_by_id(self, user_id: int):
        pass

    async def get_all_user(self):
        pass

    async def check_user_by_id(self, user_id: int):
        pass


@repository_log(exception_log)
class UserRepository(UserBaseRepository):
    def __init__(self, db: AsyncSession) -> None:
        self.db = db

    async def get_user_password(self, email: str) -> UserInternal | None:
        query = await self.db.execute(select(UserModel).where(UserModel.email == email))
        result = query.scalar_one_or_none()

        if result is None:
            return None
        return UserInternal.model_validate(result)

    async def get_user_by_email(self, email: str) -> UserReturn | None:

        query = await self.db.execute(select(UserModel).where(UserModel.email == email))
        result = query.scalar_one_or_none()

        if result is None:
            return None
        return UserReturn.model_validate(result)

    async def get_all_user(self) -> List[UserReturn] | None:

        query = await self.db.execute(select(UserModel))
        results = query.scalars().all()

        if not results:
            return None

        return [UserReturn.model_validate(result) for result in results]

    async def get_user_by_id(self, user_id: int) -> UserReturn | None:
        query = await self.db.execute(select(UserModel).where(UserModel.id == user_id))
        result = query.scalar_one_or_none()

        if result is None:
            return None

        return UserReturn.model_validate(result)

    async def check_user_by_id(self, user_id: int) -> bool | None:
        try:
            return await self.db.scalar(select(exists().where(UserModel.id == user_id)))
        except Exception as error:
            logging.error(f"Error: {error}")
            raise error

    async def create_user(self, user: UserCreate) -> None:
        self.db.add(UserModel(**user.model_dump()))

    async def update_user_by_id(self, user_id: int, user: UserUpdate) -> bool:
        result = await self.db.execute(
            update(UserModel)
            .where(UserModel.id == user_id)
            .values(**user.model_dump(exclude_unset=True))
        )

        return result.rowcount == 1

    async def delete_user_by_id(self, user_id: int) -> bool:
        result = await self.db.execute(delete(UserModel).where(UserModel.id == user_id))

        return result.rowcount == 1
