from fastapi import APIRouter, Depends, HTTPException, status

from core.models import db_helper
from core.schemas.post import PostCreate, Post
from crud import posts as posts_crud
from crud import users as users_crud


router = APIRouter(prefix="/posts", tags=["Posts"])


@router.post("/{username}", response_model=PostCreate)
async def create_post(
    post: PostCreate,
    username: str,
    session=Depends(db_helper.session_getter),
):
    user = await users_crud.get_user_by_username(session=session, username=username)

    await posts_crud.create_post(
        session=session,
        post=post,
        user_id=user.id,
    )

    return PostCreate(
        user_id=post.user_id,
        text=post.text,
    )


@router.get("/{post_id}/", response_model=Post)
async def get_post(
    post_id: int,
    session=Depends(db_helper.session_getter),
):
    post = await posts_crud.get_post_by_id(
        session=session,
        post_id=post_id,
    )
    if post is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Post #{post_id} not found",
        )

    return post


@router.delete("/{post_id}/")
async def delete_post(
    post_id: int,
    session=Depends(db_helper.session_getter),
):
    await posts_crud.delete_post_by_id(
        session=session,
        post_id=post_id,
    )

    return f"post #{post_id} wa deleted!"
