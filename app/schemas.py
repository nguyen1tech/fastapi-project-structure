from pydantic import BaseModel


class ErrorItem(BaseModel):
    error_code: str
    error_message: str


class ErrorResponse(BaseModel):
    errors: list[ErrorItem]
