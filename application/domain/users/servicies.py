from typing import Optional

from pydantic import EmailStr

from ..errors import EntityError
from ..types import Service
from .entities import User
from .repositories import UserRepository
from .types import UserName


class UserService(Service):
    def __init__(self, user_repo: UserRepository) -> None:
        self.user_repo = user_repo

    def register_user(self, email: EmailStr, name: Optional[UserName] = None) -> User:
        user_data = dict(email=email)
        if name is not None:
            user_data["name"] = name

        user = User(**user_data)
        repo_user_id = self.user_repo.insert(user)
        # TODO: add addition logic like send email etc
        return self.user_repo.get_by_id(repo_user_id)

    def have_users(self) -> bool:
        return self.user_repo.get_count() > 0
