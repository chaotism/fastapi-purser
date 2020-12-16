from typing import Optional
from datetime import datetime

from pydantic import Field

from ..types import Entity
from ..accounts import Account, Money
from .defines import StatusType
from .types import TransactionID


class Transaction(Entity):
    id: Optional[TransactionID] = Field(alias='_id')

    from_account: Account  # TODO: use only id
    to_account: Account  # TODO: use only id

    sum: Money

    status: Optional[str] = StatusType.new.value  # TODO: fix working with Enum
    error: Optional[str] = None
    completed_at: Optional[datetime] = None

    def set_complete(self):
        self.status = StatusType.success.value
        self.completed_at = datetime.now()

    def set_failed(self, err: str = None):
        self.status = StatusType.failed.value
        self.error = err
        self.completed_at = datetime.now()
