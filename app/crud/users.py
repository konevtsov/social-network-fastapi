from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.engine import Result
from sqlalchemy import select

from core.models import User
from core.schemas.user import UserCreate


async def create_user(session: AsyncSession, user: UserCreate) -> User:
    user = User(username=user.username)
    session.add(user)
    await session.commit()

    return user


async def get_user_by_username(session: AsyncSession, username: str) -> User | None:
    stmt = select(User).where(username == User.username)
    result: Result = await session.execute(stmt)
    user: User | None = result.scalar_one_or_none()

    return user
