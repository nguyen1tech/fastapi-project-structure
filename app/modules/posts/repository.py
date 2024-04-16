from contextlib import AbstractContextManager
from typing import Callable

from sqlalchemy.orm import Session

from app.exceptions import NotFoundError
from app.modules.posts.models import Post


class PostRepository:

    def __init__(
        self, session_factory: Callable[..., AbstractContextManager[Session]]
    ) -> None:
        self.session_factory = session_factory

    def insert(self, author_id: int, title: str, content: str) -> Post:
        post = Post(author_id=author_id, title=title, content=content)
        with self.session_factory() as session:
            session.add(post)
            session.commit()
            session.refresh(post)
            return post

    def get_by_id(self, post_id: int) -> Post:
        with self.session_factory() as session:
            post = session.query(Post).filter(Post.id == post_id).first()
            if not post:
                raise NotFoundError("Post not found")
            return post
