from typing import Optional
from decimal import Decimal

from .defines import CurrencyType
from .types import AccountID
from ..users.entities import User
from ...types import Entity


class Money(Entity):
    amount: Decimal
    currency: CurrencyType


class Account(Entity):
    _id: Optional[AccountID]
    owner: User

    balance: Money
