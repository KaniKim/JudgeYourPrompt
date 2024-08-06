from fastapi import Depends

from service.novel import NovelService
from repository.novel import NovelRepository
from session.manager import get_db


class UserFactory:
    """
    This is the factory container that will instantiate all the controllers and
    repositories which can be accessed by the rest of the application.
    """

    novel_repository = NovelRepository

    def get_novel_service(self, db_session=Depends(get_db)):
        return NovelService(novel_repository=self.novel_repository(db=db_session))
