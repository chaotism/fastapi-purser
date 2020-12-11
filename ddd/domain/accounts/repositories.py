from dataclasses import dataclass
from datetime import datetime
from decimal import Decimal
from typing import Dict, List, Optional, Generic
from uuid import UUID
from contextlib import contextmanager
from abc import ABCMeta, abstractmethod

from .defines import CurrencyType
from .entities import Account
from .types import AccountID
from ..users.entities import User

from pydantic import BaseModel, EmailStr, UUID1


class AccountRepository:
    __metaclass__ = ABCMeta

    @abstractmethod
    def get_by_id(self, instance_id: AccountID) -> Optional[Account]:
        pass

    @abstractmethod
    def get_or_raise_by_id(self, instance_id: AccountID) -> Account:
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
