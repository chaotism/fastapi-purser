from typing import Any

from fastapi import APIRouter

from config import openapi_config
from .schemas import Msg


router = APIRouter()


@router.post('/system-status/', response_model=Msg, status_code=200)
def check_app_status() -> Any:
    """
    Check app status.
    # Check DB
    # Check worker
    """
    # TODO: Not Implemented
    return {'msg': 'Ok'}


@router.post('/app-version/', response_model=Msg, status_code=200)
def check_app_version() -> Any:
    """
    Check app version.
    """
    # TODO: Not Implemented
    return {'msg': openapi_config.version}
