from typing import Any, Dict, Optional

from server.core.security.auths import verify_password

from server.routers.api.crud.base import CRUDBase
from server.routers.api.schemas.user import UserBase


class CRUDUser(CRUDBase):
    def get_by_email(self, *, email: str) -> Optional[Dict[str, Any]]:
        users = [user for user in self.model if user.get('email') == email]
        if users:
            return users[0]

    def authenticate(self, *, email: str, password: str) -> Optional[Dict[str, Any]]:
        user = self.get_by_email(email=email)
        if not user:
            return None
        if not verify_password(password, user.hashed_password):
            return None
        return user

    def is_active(self, user: UserBase) -> bool:
        return user.is_active

    def is_superuser(self, user: UserBase) -> bool:
        return user.is_superuser


user = CRUDUser({})
