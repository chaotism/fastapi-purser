from typing import Optional

from pydantic import EmailStr

from ..types import Entity
from .types import UserID, UserName


class User(Entity):
    id: Optional[UserID]
    email: EmailStr
    name: Optional[UserName] = None
    is_super_user: Optional[bool] = False

    @staticmethod
    def is_superuser(self) -> bool:
        return self.is_super_user

    @staticmethod
    def is_himself(self, user_id: UserID) -> bool:
        return self.id == user_id
