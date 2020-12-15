from typing import Any, List
from pydantic import BaseModel

from domain.users import UserID
from domain.accounts import Account
from pydantic import BaseModel
from ..transactions.schemas import StoredTransaction


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
class StoredTransactions(BaseModel):
    transactions = List[StoredTransaction]
