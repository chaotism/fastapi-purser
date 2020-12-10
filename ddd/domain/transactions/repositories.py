from dataclasses import dataclass
from datetime import datetime
from decimal import Decimal
from typing import Dict, List, Optional, Generic
from uuid import UUID

from .entities import Transaction
from .types import TransactionID
from ..users.entities import User

from pydantic import BaseModel, EmailStr, UUID1


class TransactionRepository:
    def get_by_id(self, instance_id: TransactionID) -> Optional[Transaction]:
        pass

    def get_or_raise_by_id(self, instance_id: TransactionID) -> Transaction:
        pass

    def insert(self, instance: Transaction) -> None:
        pass

    def update(self, instance: Transaction) -> None:
        pass

    def delete(self, instance: Transaction) -> None:
        pass
