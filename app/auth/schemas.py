from pydantic import BaseModel


class LoginRequest(BaseModel):
    email: str
    password: str


class RegisteRequest(BaseModel):
    email: str
    password: str
    name: str


class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"


# Contents of JWT token
class TokenPayload(BaseModel):
    sub: str | None = None


class UserInfoResponse(BaseModel):
    id: int
    email: str
    name: str
