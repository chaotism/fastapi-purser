from dataclasses import dataclass
from datetime import datetime
from decimal import Decimal
from typing import Dict, List, Optional, Generic
from uuid import UUID

from .entities import User
from .types import UserID
from ..users.entities import User

from pydantic import BaseModel, EmailStr, UUID1


class UserRepository:
    def get_by_id(self, instance_id: UserID) -> Optional[User]:
        pass

    def get_or_raise_by_id(self, instance_id: UserID) -> User:
        pass

    def insert(self, instance: User) -> None:
        pass

    def update(self, instance: User) -> None:
        pass

    def delete(self, instance: User) -> None:
        pass
