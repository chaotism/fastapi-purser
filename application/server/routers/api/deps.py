from typing import Generator

from fastapi import Depends, HTTPException, status
from pydantic import ValidationError

from server.routers.api import schemas
from server.routers.api import crud
from server.core import security


def get_users_db() -> Generator:  # TODO: use try DB
    try:
        yield crud.user.model
    finally:
        for key in crud.user.model:
            crud.user.model.pop(key)


def get_current_user(
    token: str,
    db: dict = Depends(get_users_db),
) -> schemas.user.UserInDB:
    try:
        payload = jwt.decode(
            token, settings.SECRET_KEY, algorithms=[security.ALGORITHM]
        )
        token_data = schemas.TokenPayload(**payload)
    except (jwt.JWTError, ValidationError):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Could not validate credentials",
        )
    user = crud.user.get(db, id=token_data.sub)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user


def get_current_active_user(
    current_user: models.User = Depends(get_current_user),
) -> models.User:
    if not crud.user.is_active(current_user):
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user


def get_current_active_superuser(
    current_user: models.User = Depends(get_current_user),
) -> models.User:
    if not crud.user.is_superuser(current_user):
        raise HTTPException(
            status_code=400, detail="The user doesn't have enough privileges"
        )
    return current_user
