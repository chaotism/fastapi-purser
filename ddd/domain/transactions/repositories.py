from dataclasses import dataclass
from datetime import datetime
from decimal import Decimal
from typing import Dict, List, Optional, Generic
from uuid import UUID
from contextlib import contextmanager
from abc import ABCMeta, abstractmethod

from .entities import Transaction
from .types import TransactionID
from ..users.entities import User
from ...types import Repository

from pydantic import BaseModel, EmailStr, UUID1


class TransactionRepository(Repository):
    __metaclass__ = ABCMeta

    @abstractmethod
    def get_by_id(self, instance_id: TransactionID) -> Optional[Transaction]:
        pass

    @abstractmethod
    def get_or_raise_by_id(self, instance_id: TransactionID) -> Transaction:
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
