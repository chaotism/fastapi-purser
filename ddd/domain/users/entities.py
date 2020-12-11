from typing import Optional

from pydantic import EmailStr, UUID1

from .types import UserName
from ...types import Entity


class User(Entity):
    _id: UUID1
    email: EmailStr
    name: Optional[UserName] = None
