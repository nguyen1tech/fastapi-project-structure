from pydantic import BaseModel


class CreateUserRequest(BaseModel):
    email: str
    password: str
    name: str


class CreateUserResponse(BaseModel):
    user_id: int


class GetUserResponse(BaseModel):
    user_id: int
    email: str


class GetListUsersResponse(BaseModel):
    ok: bool
    data: list[GetUserResponse]
