from pydantic import BaseModel
from datetime import datetime


class UserBase(BaseModel):
    email: str
    password: str


class UserCreate(UserBase):
    nick_name: str | None = None
    first_name: str | None = None
    last_name: str | None = None
    phone_number: str | None = None


class UserUpdate(UserBase):
    nick_name: str | None
    first_name: str | None
    last_name: str | None
    phone_number: str | None


class UserDBBase(UserBase):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True


class User(UserDBBase):
    nick_name: str | None
    first_name: str | None
    last_name: str | None
    phone_number: str | None


class UserInDB(UserDBBase):
    nick_name: str | None
    first_name: str | None
    last_name: str | None
    phone_number: str | None
