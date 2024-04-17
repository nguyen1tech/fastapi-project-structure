from contextlib import AbstractContextManager
from typing import Callable

from sqlalchemy.orm import Session

from app.exceptions import NotFoundError
from app.modules.tags.models import Tag


class TagRepository:

    def __init__(
        self, session_factory: Callable[..., AbstractContextManager[Session]]
    ) -> None:
        self.session_factory = session_factory

    def insert(self, user_id: int, name: str, description: str) -> Tag:
        tag = Tag(user_id=user_id, name=name, description=description)
        with self.session_factory() as session:
            session.add(tag)
            session.commit()
            session.refresh(tag)
            return tag

    def get_by_id(self, tag_id: int) -> Tag:
        with self.session_factory() as session:
            tag = session.query(Tag).filter(Tag.id == tag_id).first()
            if not tag:
                raise NotFoundError("Tag not found")
            return tag
