from typing import Any
from fastapi import APIRouter, Depends, status

from dependency_injector.wiring import inject, Provide

from app.containers import Container
from app.auth.dependencies import get_current_active_user
from app.modules.posts.schemas import (
    CreatePostRequest,
    CreatePostResponse,
    GetPostResponse,
)
from app.modules.posts.service import PostService
from app.users.models import User


router = APIRouter()


@router.post(
    "/posts",
    status_code=status.HTTP_201_CREATED,
    response_model=CreatePostResponse,
)
@inject
def create_post(
    request: CreatePostRequest,
    current_user: User = Depends(get_current_active_user),
    post_service: PostService = Depends(Provide[Container.post_service]),
) -> Any:
    post_id = post_service.create_post(
        author_id=current_user.id, post_request=request
    )
    return CreatePostResponse(id=post_id)


@router.get(
    "/posts/{post_id}",
    status_code=status.HTTP_200_OK,
    response_model=GetPostResponse,
)
@inject
def get_post_by_id(
    post_id: int,
    post_service: PostService = Depends(Provide[Container.post_service]),
) -> Any:
    post = post_service.get_post_by_id(post_id=post_id)
    return GetPostResponse(id=post.id, title=post.title, content=post.content)
