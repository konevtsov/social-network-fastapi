from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from .base import Base
from .mixins import UserRelationMixin


class Post(Base, UserRelationMixin):
    _user_back_populates = "posts"

    text: Mapped[str] = mapped_column(String(100))
