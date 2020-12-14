from typing import Optional

from .defines import StatusType
from .types import TransactionID
from ..accounts.entities import Account, Money
from ...domain.types import Entity


# TODO: use pydantic types

class Transaction(Entity):
    id: Optional[TransactionID]

    from_account: Account
    to_account: Account

    sum: Money

    status: Optional[StatusType] = StatusType('new')
