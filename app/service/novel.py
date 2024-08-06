from typing import List

from schema.novel import NovelReturn, NovelUpdate
from session.transactional import transactional
from repository.novel import NovelRepository


class NovelService:
    def __init__(self, novel_repository: NovelRepository):
        self._novel_repo = novel_repository

    @transactional
    async def get_novel(self, novel_id: int) -> NovelReturn | None:
        return await self._novel_repo.get_novel_by_id(novel_id=novel_id)

    @transactional
    async def get_novel_by_user_id(self, user_id: int) -> List[NovelReturn] | None:
        return await self._novel_repo.get_novels_by_user(user_id=user_id)

    @transactional
    async def update_novel(
        self, user_id: int, novel_id: int, novel: NovelUpdate
    ) -> bool | None:
        if await self._novel_repo.check_novel_is_user_novel(
            user_id=user_id, novel_id=novel_id
        ):
            return await self._novel_repo.update_novel_by_id(
                novel_id=novel_id, novel=novel
            )
        return None

    @transactional
    async def delete_novel(self, novel_id: int) -> bool:
        if await self._novel_repo.delete_novel_by_id(novel_id=novel_id):
            return await self._novel_repo.delete_novel_by_id(novel_id=novel_id)
        return False
