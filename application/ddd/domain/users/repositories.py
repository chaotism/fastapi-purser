from abc import ABCMeta, abstractmethod
from contextlib import contextmanager
from typing import Optional

from .types import UserID
from ..users.entities import User
from ...types import Repository


class UserRepository(Repository):
    __metaclass__ = ABCMeta

    @abstractmethod
    def get_by_id(self, instance_id: UserID) -> Optional[User]:
        pass

    @abstractmethod
    def insert(self, instance: User) -> None:
        pass

    @abstractmethod
    def update(self, instance: User) -> None:
        pass

    @abstractmethod
    def delete(self, instance: User) -> None:
        pass

    @abstractmethod
    @contextmanager
    def atomic(self):
        pass
