from typing import Any
from fastapi import APIRouter, status, Depends
from dependency_injector.wiring import inject, Provide

from app.containers import Container
from app.users.schemas import (
    CreateUserRequest,
    CreateUserResponse,
    GetListUsersResponse,
    GetUserResponse,
)
from app.users.service import UserService


router = APIRouter()


@router.post(
    "/users",
    status_code=status.HTTP_201_CREATED,
    response_model=CreateUserResponse,
)
@inject
def create_user(
    request: CreateUserRequest,
    user_service: UserService = Depends(Provide[Container.user_service]),
) -> Any:
    user = user_service.create_user(
        email=request.email, password=request.password, name=request.name
    )
    return CreateUserResponse(user_id=user.id)


@router.get(
    "/users",
    status_code=status.HTTP_200_OK,
    response_model=GetListUsersResponse,
)
@inject
def get_users(
    user_service: UserService = Depends(Provide[Container.user_service]),
) -> Any:
    users = user_service.get_users()
    user_responses = [
        GetUserResponse(user_id=user.id, email=user.email) for user in users
    ]
    return GetListUsersResponse(ok=True, data=user_responses)


@router.get(
    "/users/{user_id}",
    status_code=status.HTTP_200_OK,
    response_model=GetUserResponse,
)
@inject
def get_by_user_id(
    user_id: int,
    user_service: UserService = Depends(Provide[Container.user_service]),
) -> Any:
    user = user_service.get_user_by_id(user_id=user_id)
    return GetUserResponse(user_id=user.id, email=user.email)


@router.delete("/users/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
@inject
def delete_by_user_id(
    user_id: int,
    user_service: UserService = Depends(Provide[Container.user_service]),
) -> None:
    user_service.delete_user_by_id(user_id=user_id)
