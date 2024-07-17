from fastapi import APIRouter, Depends, status, HTTPException

from core.models import db_helper
from crud import users as users_crud
from core.schemas.user import UserCreate


router = APIRouter(prefix="/user", tags=["Users"])


@router.get("/{username}")
async def create_user(
    username: str,
    session=Depends(db_helper.session_getter),
):
    user = await users_crud.get_user_by_username(
        session=session,
        username=username,
    )

    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"{username} not found",
        )
    return user


@router.post("/create", response_model=UserCreate)
async def create_user(
    username: str,
    session=Depends(db_helper.session_getter),
):
    user_exist = await users_crud.get_user_by_username(
        session=session,
        username=username,
    )
    if not user_exist:
        user = UserCreate(
            username=username,
        )
        await users_crud.create_user(
            session=session,
            user=user,
        )
    else:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="User already exists",
        )

    return user
