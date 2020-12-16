from typing import Any

from fastapi import APIRouter, Depends, HTTPException

from domain.users import UserService, UserID
from .deps import get_users_service
from .schemas import UserCreate, StoredUser

router = APIRouter()


# TODO: add checking current user


@router.get('/{user_id}', response_model=StoredUser)
async def get_user(
    user_id: UserID,
    user_service: UserService = Depends(get_users_service),
) -> Any:
    """
    Get a specific user by id.
    """
    user = await user_service.user_repo.get_by_id(instance_id=user_id)
    if not user:
        raise HTTPException(
            status_code=404,
            detail='Not found',
        )
    return user


@router.post('/', response_model=StoredUser)
async def create_user(
    *,
    user_service: UserService = Depends(get_users_service),
    user_in: UserCreate,
) -> Any:
    """
    Create new user.
    """
    existing_user = await user_service.user_repo.get_by_email(email=user_in.email)
    if existing_user:
        raise HTTPException(  # TODO: move checking into services
            status_code=400,
            detail='The user with this email already exists in the system.',
        )
    user = await user_service.register_user(user_in.email, user_in.name)
    return user
