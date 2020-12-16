from typing import Optional, Type

from pydantic import EmailStr

from ..types import Service
from .entities import User
from .repositories import UserRepository
from .types import UserName


class UserService(Service):
    def __init__(self, user_repo: Type[UserRepository]) -> None:
        self.user_repo = user_repo

    async def register_user(
        self, email: EmailStr, name: Optional[UserName] = None
    ) -> User:
        user_data = dict(email=email)
        if name is not None:
            user_data["name"] = name

        user = User(**user_data)
        async with self.user_repo.atomic():
            repo_user_id = await self.user_repo.insert(user)
            return await self.user_repo.get_by_id(repo_user_id)

    async def have_users(self) -> bool:
        return await self.user_repo.get_count() > 0
