from abc import ABC
from typing import List

from sqlalchemy import delete, exists, select, update
from sqlalchemy.ext.asyncio import AsyncSession

from schema.novel import NovelCreate, NovelReturn, NovelUpdate
from model.novel import Novel as NovelModel
from model.user import User as UserModel


class NovelBaseRepository(ABC):

    async def get_novels_by_user(self, user_id: int):
        pass

    async def get_novel_by_id(self, user_id: int):
        pass

    async def create_novel(self, novel: NovelCreate):
        pass

    async def update_novel_by_id(self, novel_id: int, novel: NovelUpdate):
        pass

    async def delete_novel_by_id(self, novel_id: int):
        pass


class NovelRepository(NovelBaseRepository):
    def __init__(self, db: AsyncSession) -> None:
        self.db = db

    async def check_novel_is_user_novel(self, novel_id: int, user_id: int) -> bool:
        query = await self.db.execute(
            select(NovelModel)
            .where(NovelModel.id == novel_id)
            .where(NovelModel.user_id == user_id)
        )

        return query.scalar_one_or_none() is not None

    async def get_novel_by_id(self, novel_id: int) -> NovelReturn | None:
        query = await self.db.execute(
            select(NovelModel).where(NovelModel.id == novel_id)
        )
        result = query.scalar_one_or_none()

        if result is None:
            return None
        return NovelReturn.model_validate(result)

    async def get_novels_by_user(self, user_id: int) -> List[NovelReturn] | None:
        query = await self.db.execute(
            select(NovelModel).where(NovelModel.user_id == user_id)
        )
        results = query.scalars().all()
        if not results:
            return None
        return [NovelReturn.model_validate(result) for result in results]

    async def create_novel(self, novel: NovelCreate) -> None:
        self.db.add(NovelModel(**novel.model_dump()))

    async def update_novel_by_id(
        self, novel_id: int, novel: NovelUpdate
    ) -> bool | None:
        result = await self.db.execute(
            update(NovelModel)
            .where(NovelModel.id == novel_id)
            .values(**novel.model_dump())
        )

        return result.rowcount == 1

    async def delete_novel_by_id(self, novel_id: int) -> bool:
        result = await self.db.execute(
            delete(NovelModel).where(NovelModel.id == novel_id)
        )

        return result.rowcount == 1
