from typing import Optional

from pydantic import UUID1

from .defines import StatusType
from ..accounts.entities import Account, Money
from ...types import Entity


# TODO: use pydantic types

class Transaction(Entity):
    _id: UUID1

    from_account: Account
    to_account: Account

    sum: Money

    status: Optional[StatusType] = StatusType('new')
