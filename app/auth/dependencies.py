from fastapi import Depends
from dependency_injector.wiring import Provide, inject
from jose import jwt
from pydantic import ValidationError

from app.containers import Container
from app.auth.schemas import TokenPayload
from app.core.security import JWTBearer, decode_jwt_token
from app.exceptions import AuthenticationError
from app.users.models import User
from app.users.service import UserService


@inject
def get_current_active_user(
    token: str = Depends(JWTBearer(auto_error=False)),
    service: UserService = Depends(Provide[Container.user_service]),
) -> User:
    try:
        payload = decode_jwt_token(token=token)
        token_payload = TokenPayload(**payload)
    except (jwt.JWTError, ValidationError) as e:
        raise AuthenticationError("Could not validate credentials") from e
    current_user: User = service.get_user_by_email(token_payload.sub)
    if not current_user:
        raise AuthenticationError("User not found")
    return current_user
