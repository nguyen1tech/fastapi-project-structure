from contextlib import AbstractContextManager
from typing import Callable

from sqlalchemy.orm import Session

from app.exceptions import NotFoundError
from app.users.models import User


class UserRepository:

    def __init__(
        self, session_factory: Callable[..., AbstractContextManager[Session]]
    ) -> None:
        self.session_factory = session_factory

    def insert(self, email: str, password: str, is_active: bool = True) -> User:
        with self.session_factory() as session:
            user = User(email=email, password=password, is_active=is_active)
            session.add(user)
            session.commit()
            session.refresh(user)
            return user

    def get_all(self) -> list[User]:
        with self.session_factory() as session:
            return session.query(User).all()

    def get_by_id(self, user_id: int) -> User:
        with self.session_factory() as session:
            user = session.query(User).filter(User.id == user_id).first()
            if not user:
                raise NotFoundError("User not found")
            return user

    def delete_by_id(self, user_id: int) -> None:
        pass
