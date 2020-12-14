from typing import Optional

from pydantic import EmailStr

from .types import UserID, UserName
from ...domain.types import Entity


class User(Entity):
    id: Optional[UserID]
    email: EmailStr
    name: Optional[UserName] = None
