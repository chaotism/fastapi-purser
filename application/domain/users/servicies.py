from typing import Optional

from pydantic import EmailStr

from .repositories import UserRepository
from .types import UserName
from ..users import User
from ..types import Service
from ..errors import EntityError


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

    @staticmethod
    def is_yourself(you: User, checking_user: User) -> bool:
        if you.id is None:
            raise EntityError("you haven't id'")
        if checking_user.id is None:
            raise EntityError("checking_user haven't id'")
        return you.id == checking_user.id

    @staticmethod
    def is_superuser(checking_user: User) -> bool:
        return checking_user.is_super_user

    def have_users(self) -> bool:
        return self.user_repo.get_count() > 0
