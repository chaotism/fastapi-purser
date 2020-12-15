from pydantic import BaseModel

from domain.transactions import Transaction
from domain.types import PDObjectId


# Properties to receive on transaction creation
class TransactionCreate(BaseModel):
    from_account_id: PDObjectId
    to_account_id: PDObjectId

    sum: float


# Properties to return to client
class StoredTransaction(Transaction):
    pass
