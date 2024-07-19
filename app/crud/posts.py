from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.engine import Result
from sqlalchemy import select, delete

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


async def get_post_by_id(session: AsyncSession, post_id: int) -> Post:
    stmt = select(Post).where(Post.id == post_id)
    result: Result = await session.execute(stmt)

    return result.scalar_one_or_none()


async def delete_post_by_id(session: AsyncSession, post_id: int) -> None:
    stmt = delete(Post).where(Post.id == post_id)
    await session.execute(stmt)
    await session.commit()
