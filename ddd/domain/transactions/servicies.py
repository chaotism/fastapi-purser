from dataclasses import dataclass
from datetime import datetime
from decimal import Decimal
from typing import Dict, List, Optional
from uuid import UUID

from .defines import StatusType
from .entities import Transaction, Money
from .repositories import TransactionRepository
from .types import TransactionID
from ..accounts.entities import Account
from ..users.entities import User

from pydantic import BaseModel, EmailStr, UUID1


class TransactionService:
    def __init__(self) -> None:
        self.transaction_repo = TransactionRepository()

    def register_transaction(
        self, transaction_id: TransactionID, from_account: Account, to_account: Account, sum: Money
    ) -> Transaction:
        transaction = Transaction(_id=transaction_id, from_account=from_account, to_account=to_account, sum=sum)  # TODO: create id after save
        self.transaction_repo.insert(transaction)
        return transaction

    def evaluate_transaction(self, transaction_id: TransactionID) -> StatusType:
        transaction = self.transaction_repo.get_by_id(transaction_id)  # TODO: make idea of commit level
        raise NotImplemented
