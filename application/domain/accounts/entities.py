from typing import Optional
from decimal import Decimal

from pydantic import BaseModel

from ..users import User
from ..errors import EntityError
from ..types import Entity
from .defines import CurrencyType
from .types import AccountID


class Money(BaseModel):
    amount: Decimal
    currency: Optional[CurrencyType] = CurrencyType.usd


class Account(Entity):
    id: Optional[AccountID]
    owner: User

    balance: Money

    def is_owner(self, user: User) -> bool:
        if self.owner.id is None:
            raise EntityError("account owner haven't id'")
        if user.id is None:
            raise EntityError("checking_user haven't id'")
        return self.owner.id == user.id
