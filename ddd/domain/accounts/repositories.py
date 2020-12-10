from dataclasses import dataclass
from datetime import datetime
from decimal import Decimal
from typing import Dict, List, Optional, Generic
from uuid import UUID

from .defines import CurrencyType
from .entities import Account
from .types import AccountID
from ..users.entities import User

from pydantic import BaseModel, EmailStr, UUID1


class AccountRepository:
    def get_by_id(self, instance_id: AccountID) -> Optional[Account]:
        pass

    def get_or_raise_by_id(self, instance_id: AccountID) -> Account:
        pass

    def insert(self, instance: Account) -> None:
        pass

    def update(self, instance: Account) -> None:
        pass

    def delete(self, instance: Account) -> None:
        pass
