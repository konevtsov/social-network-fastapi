from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.engine import Result
from sqlalchemy import select

from core.models import Post
from core.schemas.post import PostCreate


async def create_post(session: AsyncSession, post: PostCreate, user_id: int) -> Post:
    post = Post(
        text=post.text,
        user_id=user_id,
    )
    session.add(post)
    await session.commit()

    return post
