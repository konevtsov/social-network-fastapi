from fastapi import APIRouter, Depends

from core.models import db_helper
from core.schemas.post import PostCreate
from crud import posts as posts_crud
from crud import users as users_crud


router = APIRouter(prefix="/posts", tags=["Posts"])


@router.post("/create/{username}", response_model=PostCreate)
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
