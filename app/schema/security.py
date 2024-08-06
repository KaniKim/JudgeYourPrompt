from pydantic import BaseModel


class Token(BaseModel):
    access_token: str
    token_type: str
    refresh_token: str


class TokenPayload(BaseModel):
    email: str
    exp: str
