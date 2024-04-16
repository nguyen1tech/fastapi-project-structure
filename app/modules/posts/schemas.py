from pydantic import BaseModel


class CreatePostRequest(BaseModel):
    title: str
    content: str


class CreatePostResponse(BaseModel):
    id: int


class GetPostResponse(BaseModel):
    id: int
    title: str
    content: str
