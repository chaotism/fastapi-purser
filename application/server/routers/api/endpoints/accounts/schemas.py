from pydantic import BaseModel

from domain.accounts import Account
from domain.types import PDObjectId
from pydantic import BaseModel, EmailStr


# Properties to receive on user creation
class AccountCreate(BaseModel):
    owner_id: PDObjectId
    balance: float


# Properties to return to client
class StoredAccount(Account):
    pass


# Properties to receive on account deposit
class DepositMoney(BaseModel):
    sum: float

