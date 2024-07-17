from pydantic import BaseModel, Field


class PostBase(BaseModel):
    user_id: int
    text: str = Field(max_length=100)


class PostCreate(PostBase):
    pass
