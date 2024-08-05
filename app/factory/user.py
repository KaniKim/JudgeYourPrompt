from fastapi import Depends
from service.token import TokenService
from repository.user import UserRepository
from service.user import UserService
from session.manager import get_db


class Factory:
    """
    This is the factory container that will instantiate all the controllers and
    repositories which can be accessed by the rest of the application.
    """

    user_repository = UserRepository

    def get_user_service(self, db_session=Depends(get_db)):
        return UserService(user_repository=self.user_repository(db=db_session))

    def get_token_service(self, db_sesion=Depends(get_db)):
        return TokenService(user_repository=self.user_repository(db=db_sesion))
