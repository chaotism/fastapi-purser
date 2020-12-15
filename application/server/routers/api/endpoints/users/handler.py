from typing import Any

from fastapi import APIRouter, Depends, HTTPException

from domain.types import PDObjectId
from domain.users import UserService
from .deps import get_users_service
from .schemas import UserCreate, StoredUser

router = APIRouter()


# TODO: add checking current user


@router.post('/', response_model=StoredUser)
def create_user(
    *,
    user_service: UserService = Depends(get_users_service),
    user_in: UserCreate,
) -> Any:
    """
    Create new user.
    """
    user = user_service.user_repo.get_by_email(email=user_in.email)
    if user:
        raise HTTPException(
            status_code=400,
            detail='The user with this username already exists in the system.',
        )
    user = user_service.register_user(user_in.email, user_in.name)
    return user


@router.get('/{user_id}', response_model=StoredUser)
def read_user_by_id(
    user_id: PDObjectId,
    user_service: UserService = Depends(get_users_service),
) -> Any:
    """
    Get a specific user by id.
    """
    user = user_service.user_repo.get_by_id(instance_id=user_id)
    return user
