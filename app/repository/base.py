from typing import Generic, Type, TypeVar

from sqlalchemy.ext.asyncio import AsyncSession

from session.manager import Base


ModelType = TypeVar("ModelType", bound=Base)


class BaseRepository(Generic[ModelType]):
    def __init__(self, model: Type[ModelType], db_session: AsyncSession):
        self.session = db_session
