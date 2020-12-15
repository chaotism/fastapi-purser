from typing import Optional
from decimal import Decimal

from pydantic import BaseModel

from .defines import CurrencyType
from .types import AccountID
from ..users import User
from ..types import Entity


class Money(BaseModel):
    amount: Decimal
    currency: Optional[CurrencyType] = CurrencyType.usd


class Account(Entity):
    id: Optional[AccountID]
    owner: User

    balance: Money
