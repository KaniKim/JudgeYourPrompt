from typing import Annotated

from fastapi import APIRouter, Depends
from starlette import status
from fastapi.responses import JSONResponse, Response
from sqlalchemy.ext.asyncio import AsyncSession

from api.v1.dependencies.security import get_current_user
from factory.user import Factory
from session.manager import get_db
from schema.security import Token
from schema.user import User, UserCreate, UserUpdate
from service.token import TokenService
from service.user import UserService

user_router = APIRouter(prefix="/user", tags=["users"])


@user_router.post("/token", status_code=status.HTTP_201_CREATED, response_model=Token)
async def login_for_access_token(
    email: str,
    password: str,
    token_service: TokenService = Depends(Factory().get_token_service),
) -> Token | JSONResponse:
    if await token_service.authenticate_user(email=email, password=password):
        data = {"email": email}
        access_token = await token_service.create_access_token(data=data)
        refresh_token = await token_service.create_refresh_token(data=data)
        return Token(
            access_token=access_token, refresh_token=refresh_token, token_type="Bearer"
        )

    return JSONResponse(
        status_code=status.HTTP_401_UNAUTHORIZED,
        content={"message": "User information is not correct"},
    )


@user_router.get(
    "/{user_id}", status_code=status.HTTP_200_OK, response_model=User | None
)
async def get_user_by_id(
    user_id: int, user_service: UserService = Depends(Factory().get_user_service)
):
    return await user_service.get_user(user_id=user_id)


@user_router.post("/", status_code=status.HTTP_201_CREATED, response_model=None)
async def create_user(
    user: UserCreate, user_service: UserService = Depends(Factory().get_user_service)
):
    return await user_service.create_user(user)


@user_router.put("/{user_id}", status_code=status.HTTP_200_OK, response_model=User)
async def update_user(
    user_id: int,
    user: UserUpdate,
    user_service: UserService = Depends(Factory().get_user_service),
):
    result = await user_service.update_user(user_id=user_id, user=user)
    return result


@user_router.delete(
    "/{user_id}", status_code=status.HTTP_204_NO_CONTENT, response_class=Response
)
async def delete_user(
    user_id: int, user_service: UserService = Depends(Factory().get_user_service)
):
    if await user_service.delete_user(user_id=user_id):
        return JSONResponse(
            content={"message": "User is deleted"},
            status_code=status.HTTP_204_NO_CONTENT,
        )
    return JSONResponse(
        content={"message": "User is not deleted"},
        status_code=status.HTTP_404_NOT_FOUND,
    )


@user_router.get("/me", status_code=status.HTTP_200_OK, response_model=User)
async def get_user_me(
    token: Token, current_user: Annotated[User, Depends(get_current_user)]
):
    return current_user
