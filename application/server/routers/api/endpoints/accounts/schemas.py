from typing import List

from pydantic import BaseModel

from domain.accounts import Account
from domain.types import EncodedModel
from domain.users import UserID
from ..transactions.schemas import Transaction


# Properties to receive on user creation
class AccountCreate(BaseModel):
    owner_id: UserID
    balance: float


# Properties to return to client
class StoredAccount(Account):
    pass


# Properties to receive on account deposit
class DepositMoney(BaseModel):
    sum: float


# Properties to return to transaction client
class StoredTransactions(EncodedModel):
    transactions: List[Transaction]
