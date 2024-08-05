from fastapi import APIRouter, Depends

from api.v1.routers.user import user_router

version_router = APIRouter(prefix="/v1", tags=["v1"])
version_router.include_router(user_router)
