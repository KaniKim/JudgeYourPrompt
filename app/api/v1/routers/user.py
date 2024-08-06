from typing import Annotated, Union

from fastapi import APIRouter, Depends, Header
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from starlette import status
from fastapi.responses import JSONResponse

from factory.user import UserFactory as Factory
from schema.security import Token
from schema.user import UserCreate, UserInternal, UserReturn, UserUpdate
from service.token import TokenService
from service.user import UserService

user_router = APIRouter(prefix="/user", tags=["users"])


@user_router.get("/me", status_code=status.HTTP_200_OK)
async def get_user_me(token=Depends(Factory().get_current_user)) -> UserReturn:
    return token


@user_router.post("/token", response_model=Token)
async def login_for_access_token(
    user: UserInternal,
    token_service: TokenService = Depends(Factory().get_token_service),
) -> Token | JSONResponse:
    if await token_service.authenticate_user(email=user.email, password=user.password):
        data = {"email": user.email, "type": "access"}
        access_token = await token_service.create_access_token(data=data)
        data = {"email": user.email, "type": "refresh"}
        refresh_token = await token_service.create_refresh_token(data=data)
        return Token(
            access_token=access_token, refresh_token=refresh_token, token_type="Bearer"
        )

    return JSONResponse(
        status_code=status.HTTP_401_UNAUTHORIZED,
        content={"message": "User information is not correct"},
    )


@user_router.get(
    "/{user_id}", status_code=status.HTTP_200_OK, response_model=Union[UserReturn, None]
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


@user_router.put(
    "/{user_id}", status_code=status.HTTP_200_OK, response_model=UserReturn
)
async def update_user(
    user_id: int,
    user: UserUpdate,
    user_service: UserService = Depends(Factory().get_user_service),
):
    result = await user_service.update_user(user_id=user_id, user=user)
    return result


@user_router.delete(
    "/{user_id}", status_code=status.HTTP_204_NO_CONTENT, response_class=JSONResponse
)
async def delete_user(
    user_id: int, user_service: UserService = Depends(Factory().get_user_service)
):
    if await user_service.delete_user(user_id=user_id):
        return JSONResponse(
            content="User is deleted",
        )
    return JSONResponse(
        content="User is not deleted",
        status_code=status.HTTP_404_NOT_FOUND,
    )
