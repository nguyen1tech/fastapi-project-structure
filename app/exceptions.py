from app.constants import ErrorCode


class AppBaseError(Exception):
    error_code = ""
    error_message = ""

    def __init__(self, error_message: str = None) -> None:
        if error_message:
            self.error_message = error_message


class AuthenticationError(AppBaseError):
    error_code = ErrorCode.AUTHENTICATION_ERROR
    error_message = "Authentication error"


class NotFoundError(AppBaseError):
    error_code = ErrorCode.NOT_FOUND
    error_message = "Not found error"


class AlreadyExistsError(AppBaseError):
    error_code = ErrorCode.ALREADY_EXISTS_ERROR
    error_message = "Already exists error"
