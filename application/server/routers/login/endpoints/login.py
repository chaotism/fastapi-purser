from typing import Any
from fastapi import APIRouter, Body

from server.server.routers.login import schemas


router = APIRouter()


@router.post("/login/access-token", response_model=schemas.Token)
def login_access_token() -> Any:
    """
    OAuth2 compatible token login, get an access token for future requests
    """

    # TODO: Not implemented
    return {
        "access_token": "",
        "token_type": "bearer",
    }


@router.post("/password-recovery/{email}", response_model=schemas.Msg)
def recover_password(email: str) -> Any:
    """
    Password Recovery
    """
    # TODO: Not implemented
    return {"msg": "Password recovery email sent"}


@router.post("/reset-password/", response_model=schemas.Msg)
def reset_password(
    token: str = Body(...),
    new_password: str = Body(...),
) -> Any:
    """
    Reset password
    """
    # TODO: Not implemented
    return {"msg": "Password updated successfully"}
