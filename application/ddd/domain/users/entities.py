from typing import Optional

from pydantic import EmailStr, UUID1

from .types import UserID, UserName
from ...types import Entity


class User(Entity):
    _id: Optional[UserID]
    email: EmailStr
    name: Optional[UserName] = None
