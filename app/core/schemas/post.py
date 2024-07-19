from pydantic import BaseModel, Field


class PostBase(BaseModel):
    text: str = Field(max_length=100)


class PostCreate(PostBase):
    user_id: int


class Post(PostBase):
    id: int
    user_id: int
