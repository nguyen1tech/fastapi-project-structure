from contextlib import AbstractContextManager
from typing import Callable
from sqlalchemy.orm import Session

from app.modules.posts.repository import PostRepository

def test_insert(db_session_factory: Callable[..., AbstractContextManager[Session]]) -> None:
    post_repository = PostRepository(session_factory=db_session_factory)
    
    post = post_repository.insert(author_id=1, title="test", content="content")
    assert post is not None
    assert isinstance(post.id, int)
    
def test_get_by_id(db_session_factory: Callable[..., AbstractContextManager[Session]]) -> None:
    post_repository = PostRepository(session_factory=db_session_factory)
    
    post = post_repository.insert(author_id=1, title="test", content="content")
    assert post is not None
    assert isinstance(post.id, int)
    
    get_post = post_repository.get_by_id(post_id=post.id)
    assert get_post is not None
    assert get_post.title == post.title
    assert get_post.content == post.content
