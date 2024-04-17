from typing import Any
from fastapi import APIRouter, Depends, status

from dependency_injector.wiring import inject, Provide

from app.containers import Container
from app.auth.dependencies import get_current_active_user
from app.modules.tags.schemas import (
    CreateTagRequest,
    CreateTagResponse,
    GetTagResponse,
)
from app.modules.tags.service import TagService
from app.users.models import User


router = APIRouter()


@router.post(
    "/tags",
    status_code=status.HTTP_201_CREATED,
    response_model=CreateTagResponse,
)
@inject
def create_post(
    request: CreateTagRequest,
    current_user: User = Depends(get_current_active_user),
    tag_service: TagService = Depends(Provide[Container.tag_service]),
) -> Any:
    tag_id = tag_service.create_tag(
        user_id=current_user.id, tag_request=request
    )
    return CreateTagResponse(id=tag_id)


@router.get(
    "/tags/{tag_id}",
    status_code=status.HTTP_200_OK,
    response_model=GetTagResponse,
)
@inject
def get_tag_by_id(
    tag_id: int,
    tag_service: TagService = Depends(Provide[Container.tag_service]),
) -> Any:
    tag = tag_service.get_tag_by_id(tag_id=tag_id)
    return GetTagResponse(id=tag.id, name=tag.name, description=tag.description)
