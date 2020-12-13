from abc import ABCMeta, abstractmethod
from contextlib import contextmanager
from typing import Optional

from .entities import Transaction
from .types import TransactionID
from ...types import Repository


class TransactionRepository(Repository):
    __metaclass__ = ABCMeta

    @abstractmethod
    def get_by_id(self, instance_id: TransactionID) -> Optional[Transaction]:
        pass

    @abstractmethod
    def insert(self, instance: Transaction) -> None:
        pass

    @abstractmethod
    def update(self, instance: Transaction) -> None:
        pass

    @abstractmethod
    def delete(self, instance: Transaction) -> None:
        pass

    @abstractmethod
    @contextmanager
    def atomic(self):
        pass
