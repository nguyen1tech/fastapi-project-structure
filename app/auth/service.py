import logging

from app.exceptions import AlreadyExistsError
from app.auth.schemas import Token
from app.core.security import (
    generate_access_token,
    hash_password,
    verify_password,
)
from app.exceptions import AuthenticationError
from app.users.repository import UserRepository


logger = logging.getLogger(__name__)


class AuthService:

    def __init__(self, user_repository: UserRepository) -> None:
        self.user_repository = user_repository

    def authenticate(self, email: str, password: str) -> Token:
        logger.info("Authenticate with email: %s", email)
        user = self.user_repository.get_by_email(email=email)
        if not user:
            raise AuthenticationError("User does not exist")

        # Check password
        print(f"{password} -- {user.password}")
        if not verify_password(password, user.password):
            raise AuthenticationError("Incorrect username or password")

        # Generate jwt token
        return generate_access_token(subject=user.email)

    def register(self, email: str, password: str, name: str) -> Token:
        logger.info("Register new user with email: %s", email)
        user = self.user_repository.get_by_email(email=email)
        if user:
            raise AlreadyExistsError("Email already registered")

        user = self.user_repository.insert(
            email=email, password=hash_password(password), name=name
        )
        # Generate jwt token
        return generate_access_token(subject=user.email)
