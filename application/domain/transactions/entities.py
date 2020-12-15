from typing import Optional
from datetime import datetime

from .defines import StatusType
from .types import TransactionID
from ..accounts import Account, Money
from ..types import Entity


# TODO: use pydantic types

class Transaction(Entity):
    id: Optional[TransactionID]

    from_account: Account
    to_account: Account

    sum: Money

    status: Optional[StatusType] = StatusType('new')
    completed_at: Optional[datetime] = None
