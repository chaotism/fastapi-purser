from typing import Optional
from datetime import datetime

from pydantic import BaseModel


# Shared properties
class TransactionBase(BaseModel):
    from_user: Optional[int] = None
    to_user: Optional[int] = None
    cash: Optional[float] = None


# Properties to receive on item creation
class TransactionCreate(TransactionBase):
    from_user: int
    to_user: int
    cash: float


# Properties shared by models stored in DB
class TransactioInDBBase(BaseModel):
    id: int
    created_at: datetime
    completed_at: Optional[datetime]
    from_user: int
    to_user: int
    cash: float


# Properties to return to client
class Transaction(TransactioInDBBase):
    pass


# Properties properties stored in DB
class TransactionInDB(TransactioInDBBase):
    pass
