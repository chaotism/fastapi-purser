from typing import Optional

from pydantic import EmailStr

from .repositories import UserRepository
from .types import UserID, UserName
from ..users.entities import User
from domain.types import Service


class UserService(Service):
    def __init__(self, user_repo: UserRepository) -> None:
        self.user_repo = user_repo

    def register_user(self, email: EmailStr, name: Optional[UserName] = None) -> User:
        user_data = dict(
            email=email,
        )
        if name is not None:
            user_data['name'] = name

        user = User(**user_data)
        repo_user_id = self.user_repo.insert(user)
        # TODO: add addition logic like send email etc
        return self.user_repo.get_by_id(repo_user_id)
