from unittest import mock
from fastapi.testclient import TestClient

from app.main import app
from app.config import settings
from app.auth.dependencies import get_current_active_user
from app.modules.posts.service import PostService
from app.users.models import User
from app.modules.posts.models import Post
from app.exceptions import AlreadyExistsError


def override_get_current_active_user() -> User:
    return User(id=1, email="test@gmail.com", name="test")


def test_get_post(client: TestClient) -> None:
    mock_post = Post(id=1, author_id=1, title="test", content="test")
    mock_post_service = mock.Mock(spec=PostService)
    mock_post_service.get_post_by_id.return_value = mock_post

    with app.container.post_service.override(mock_post_service):
        response = client.get(f"{settings.API_PREFIX}/posts/1")

    assert response.status_code == 200
    content = response.json()
    assert content["id"] == mock_post.id
    assert content["title"] == mock_post.title
    assert content["content"] == mock_post.content


def test_create_post(client: TestClient) -> None:
    app.dependency_overrides[get_current_active_user] = (
        override_get_current_active_user
    )
    mock_post_service = mock.Mock(spec=PostService)
    mock_post_service.create_post.return_value = 1

    with app.container.post_service.override(mock_post_service):
        data = {"title": "Foo", "content": "Bar"}
        response = client.post(
            f"{settings.API_PREFIX}/posts",
            json=data,
        )

    assert response.status_code == 201
    content = response.json()
    assert content["id"] == 1


def test_create_post_with_exception(client: TestClient) -> None:
    app.dependency_overrides[get_current_active_user] = (
        override_get_current_active_user
    )
    mock_post_service = mock.Mock(spec=PostService)
    mock_post_service.create_post.side_effect = AlreadyExistsError("Oops!")

    with app.container.post_service.override(mock_post_service):
        data = {"title": "Foo", "content": "Bar"}
        response = client.post(
            f"{settings.API_PREFIX}/posts",
            json=data,
        )

    assert response.status_code == 400
    content = response.json()
    error = content["errors"][0]
    assert error["error_code"] == "ALREADY_EXISTS_ERROR"
    assert error["error_message"] == "Oops!"
