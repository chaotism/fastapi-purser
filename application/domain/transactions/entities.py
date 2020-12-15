from typing import Optional
from datetime import datetime
from ..types import Entity
from ..accounts import Account, Money
from .defines import StatusType
from .types import TransactionID


# TODO: use pydantic types

class Transaction(Entity):
    id: Optional[TransactionID]

    from_account: Account
    to_account: Account

    sum: Money

    status: Optional[StatusType] = StatusType('new')
    error: str
    completed_at: Optional[datetime] = None

    def set_complete(self):
        self.status = StatusType.success
        self.completed_at = datetime.now()

    def set_failed(self, err: str = None):
        self.status = StatusType.failed
        self.error = err
        self.completed_at = datetime.now()
