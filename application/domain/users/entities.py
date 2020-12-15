from typing import Optional

from pydantic import EmailStr

from ..errors import EntityError
from ..types import Entity
from .types import UserID, UserName


class User(Entity):
    id: Optional[UserID]
    email: EmailStr
    name: Optional[UserName] = None
    is_super_user: Optional[bool] = False

    def is_superuser(self) -> bool:
        return self.is_super_user

    @staticmethod
    def is_yourself(self, user_id: UserID) -> bool:
        if self.id is None:
            raise EntityError('Null id')
        return self.id == user_id
