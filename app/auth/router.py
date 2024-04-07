from typing import Any
from fastapi import APIRouter, Depends, status
from dependency_injector.wiring import Provide, inject

from app.auth.dependencies import get_current_active_user
from app.containers import Container
from app.auth.schemas import LoginRequest, RegisteRequest, UserInfoResponse
from app.auth.service import AuthService
from app.users.models import User


router = APIRouter(prefix="/auth")


@router.post("/login", status_code=status.HTTP_200_OK)
@inject
def authenticate(
    request: LoginRequest,
    auth_service: AuthService = Depends(Provide[Container.auth_service]),
) -> Any:
    return auth_service.authenticate(
        email=request.email, password=request.password
    )


@router.post("/register", status_code=status.HTTP_201_CREATED)
@inject
def register(
    request: RegisteRequest,
    auth_service: AuthService = Depends(Provide[Container.auth_service]),
) -> Any:
    return auth_service.register(
        email=request.email, password=request.password, name=request.name
    )


@router.get("/me", response_model=UserInfoResponse)
@inject
def get_me(current_user: User = Depends(get_current_active_user)) -> Any:
    return UserInfoResponse(
        id=current_user.id, email=current_user.email, name=current_user.name
    )
