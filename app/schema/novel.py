from pydantic import BaseModel
from datetime import datetime


class NovelBase(BaseModel):
    title: str


class NovelCreate(NovelBase):
    description: str | None = None


class NovelUpdate(NovelBase):
    description: str | None


class NovelReturn(NovelBase):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True
