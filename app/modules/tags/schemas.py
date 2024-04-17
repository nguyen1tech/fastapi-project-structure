from pydantic import BaseModel


class CreateTagRequest(BaseModel):
    name: str
    description: str


class CreateTagResponse(BaseModel):
    id: int


class GetTagResponse(BaseModel):
    id: int
    name: str
    description: str
