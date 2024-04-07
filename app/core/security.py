from datetime import datetime, timedelta
import logging
from typing import Any
from fastapi import Request
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer

from jose import jwt
from passlib.context import CryptContext

from app.auth.schemas import Token
from app.config import settings
from app.exceptions import AuthenticationError

logger = logging.getLogger(__name__)


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
ALGORITHM = "HS256"


def generate_access_token(subject: str | Any) -> Token:
    logger.info("Create access token for subject: %s", subject)
    expires_delta = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    expire = datetime.utcnow() + expires_delta
    to_encode = {"exp": expire, "sub": str(subject)}
    encoded_jwt = jwt.encode(
        to_encode, settings.SECRET_KEY, algorithm=ALGORITHM
    )
    return Token(access_token=encoded_jwt)


def decode_jwt_token(token: str) -> dict:
    decoded_token = jwt.decode(token, settings.SECRET_KEY, algorithms=ALGORITHM)
    return (
        decoded_token
        if decoded_token["exp"] >= int(round(datetime.utcnow().timestamp()))
        else None
    )


def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)


def hash_password(plain_password: str) -> str:
    return pwd_context.hash(plain_password)


class JWTBearer(HTTPBearer):
    def __init__(self, auto_error: bool = True):
        super(JWTBearer, self).__init__(auto_error=auto_error)

    async def __call__(self, request: Request):
        credentials: HTTPAuthorizationCredentials = await super(
            JWTBearer, self
        ).__call__(request)
        if credentials:
            if credentials.scheme != "Bearer":
                raise AuthenticationError("Invalid authentication scheme.")
            if not self.verify_jwt(credentials.credentials):
                raise AuthenticationError("Invalid token or expired token.")
            return credentials.credentials
        else:
            raise AuthenticationError("Invalid authorization code.")

    def verify_jwt(self, jwt_token: str) -> bool:
        try:
            _ = decode_jwt_token(jwt_token)
        except Exception as e:
            logger.error("Failed to decode jwt token", exc_info=e)
            return False
        return True
