import datetime
from sqlalchemy import Column, DateTime, Integer, String
from sqlalchemy.orm import relationship

from session.manager import Base  # type: ignore
from .novel import Novel  # type: ignore


class User(Base):
    __tablename__ = "user"

    id = Column(
        Integer, primary_key=True, nullable=False, autoincrement=True, unique=True
    )
    nick_name = Column(String(length=255), nullable=True)
    email = Column(String(length=255), nullable=False)
    password = Column(String(length=255), nullable=False)
    first_name = Column(String(length=255), nullable=True)
    last_name = Column(String(length=255), nullable=True)
    phone_number = Column(String(length=255), nullable=True)
    created_at = Column(DateTime(), nullable=False, default=datetime.datetime.now())
    updated_at = Column(DateTime(), nullable=False, default=datetime.datetime.now())
    novels = relationship("Novel", backref="User")
