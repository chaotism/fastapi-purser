from abc import ABCMeta, abstractmethod
from contextlib import contextmanager
from typing import Optional

from .entities import Account
from .types import AccountID
from domain.types import Repository


class AccountRepository(Repository):
    __metaclass__ = ABCMeta

    @abstractmethod
    def get_by_id(self, instance_id: AccountID) -> Optional[Account]:
        pass

    @abstractmethod
    def insert(self, instance: Account) -> None:
        pass

    @abstractmethod
    def update(self, instance: Account) -> None:
        pass

    @abstractmethod
    def delete(self, instance: Account) -> None:
        pass

    @abstractmethod
    @contextmanager
    def atomic(self):
        pass
