from fastapi import APIRouter, Depends

from api.v1 import version_router

__all__ = ["api_router"]

api_router = APIRouter(prefix="/api", tags=["api"])
api_router.include_router(version_router)
