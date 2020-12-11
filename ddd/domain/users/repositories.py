from dataclasses import dataclass
from datetime import datetime
from decimal import Decimal
from typing import Dict, List, Optional, Generic
from uuid import UUID
from contextlib import contextmanager
from abc import ABCMeta, abstractmethod

from .entities import User
from .types import UserID
from ..users.entities import User

from pydantic import BaseModel, EmailStr, UUID1


class UserRepository:
    __metaclass__ = ABCMeta

    @abstractmethod
    def get_by_id(self, instance_id: UserID) -> Optional[User]:
        pass

    @abstractmethod
    def get_or_raise_by_id(self, instance_id: UserID) -> User:
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
