__all__ = ("api_router",)

from fastapi import APIRouter

from .users import router as users_router
from .posts import router as posts_router


api_router = APIRouter()
api_router.include_router(users_router)
api_router.include_router(posts_router)
