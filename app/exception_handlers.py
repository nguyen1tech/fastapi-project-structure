from fastapi import FastAPI, Request, status
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

from app.exceptions import (
    AlreadyExistsError,
    AuthenticationError,
    NotFoundError,
)
from app.schemas import ErrorItem, ErrorResponse


def not_found_exception_handler(_: Request, exc: NotFoundError):
    error = ErrorItem(
        error_code=exc.error_code, error_message=exc.error_message
    )
    return JSONResponse(
        status_code=status.HTTP_400_BAD_REQUEST,
        content=jsonable_encoder(ErrorResponse(errors=[error])),
    )


def authentication_exception_handler(_: Request, exc: AuthenticationError):
    error = ErrorItem(
        error_code=exc.error_code, error_message=exc.error_message
    )
    return JSONResponse(
        status_code=status.HTTP_400_BAD_REQUEST,
        content=jsonable_encoder(ErrorResponse(errors=[error])),
    )


def already_exists_exception_handler(_: Request, exc: AlreadyExistsError):
    error = ErrorItem(
        error_code=exc.error_code, error_message=exc.error_message
    )
    return JSONResponse(
        status_code=status.HTTP_400_BAD_REQUEST,
        content=jsonable_encoder(ErrorResponse(errors=[error])),
    )


def register_error_handlers(app: FastAPI) -> None:
    app.add_exception_handler(NotFoundError, not_found_exception_handler)
    app.add_exception_handler(
        AuthenticationError, authentication_exception_handler
    )
    app.add_exception_handler(
        AlreadyExistsError, already_exists_exception_handler
    )
