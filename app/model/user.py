import datetime
from sqlalchemy import Column, DateTime, Integer, String

from session.manager import Base


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
