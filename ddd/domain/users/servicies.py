from typing import Optional

from pydantic import EmailStr

from .repositories import UserRepository
from .types import UserID, UserName
from ..users.entities import User
from ...types import Service


class UserService(Service):
    def __init__(self, user_repo: UserRepository) -> None:
        self.user_repo = user_repo

    def register_account(self, user_id: UserID, email: EmailStr, name: Optional[UserName] = None) -> User:
        user = User(_id=user_id, email=email, name=name)  # TODO: create id after save
        self.user_repo.insert(user)
        return user
