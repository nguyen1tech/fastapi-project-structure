import logging

from app.users.models import User
from app.users.repository import UserRepository


logger = logging.getLogger(__name__)


class UserService:

    def __init__(self, user_repository: UserRepository) -> None:
        self._repository: UserRepository = user_repository

    def create_user(self, email: str, password: str, name: str) -> User:
        logger.info("Create user with email: %s", email)
        return self._repository.insert(email=email, password=password, name=name)

    def get_users(self) -> list[User]:
        logger.info("Getting all users")
        return self._repository.get_all()

    def get_user_by_id(self, user_id: int) -> User:
        logger.info("Get user by id: %s", user_id)
        return self._repository.get_by_id(user_id)

    def get_user_by_email(self, email: str) -> User:
        logger.info("Get user by email: %s", email)
        return self._repository.get_by_email(email)

    def delete_user_by_id(self, user_id: int) -> None:
        logger.info("Delete user by id: %s", user_id)
        return self._repository.delete_by_id(user_id)
