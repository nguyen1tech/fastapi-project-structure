import pytest
from unittest import mock
from app.exceptions import AlreadyExistsError
from app.modules.posts.models import Post
from app.modules.posts.repository import PostRepository
from app.modules.posts.schemas import CreatePostRequest
from app.modules.posts.service import PostService


def test_create_post() -> None:
    mock_post_repository = mock.Mock(spec=PostRepository)
    mock_post_repository.insert.return_value = Post(
        id=1, author_id=1, title="test", content="test"
    )

    post_service = PostService(post_repository=mock_post_repository)
    post_id = post_service.create_post(
        author_id=1,
        post_request=CreatePostRequest(title="test", content="test"),
    )

    assert post_id == 1
    mock_post_repository.insert.assert_called_once()


def test_create_post_with_exception() -> None:
    mock_post_repository = mock.Mock(spec=PostRepository)
    mock_post_repository.insert.side_effect = AlreadyExistsError("Oops!")

    post_service = PostService(post_repository=mock_post_repository)

    with pytest.raises(AlreadyExistsError) as exc:
        post_service.create_post(
            author_id=1,
            post_request=CreatePostRequest(title="test", content="test"),
        )
    assert str(exc.value) == "Oops!"
