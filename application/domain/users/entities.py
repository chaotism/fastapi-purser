from typing import Optional

from pydantic import EmailStr

from ..types import Entity
from .types import UserID, UserName


class User(Entity):
    id: Optional[UserID]
    email: EmailStr
    name: Optional[UserName] = None
    is_super_user: Optional[bool] = False
