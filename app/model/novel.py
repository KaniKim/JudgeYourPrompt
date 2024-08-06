import datetime
from sqlalchemy import Column, DateTime, ForeignKey, Integer, String, Text
from sqlalchemy.orm import relationship

from session.manager import Base  # type: ignore


class Novel(Base):
    __tablename__ = "novel"

    id = Column(
        Integer, primary_key=True, nullable=False, autoincrement=True, unique=True
    )
    title = Column(String(length=255), nullable=False)
    description = Column(Text, nullable=True)
    user_id = Column(Integer, ForeignKey("user.id"), nullable=False)
    user = relationship("User", backref="Novel")
    created_at = Column(DateTime, nullable=False, default=datetime.datetime.now())
    updated_at = Column(DateTime, nullable=False, default=datetime.datetime.now())
