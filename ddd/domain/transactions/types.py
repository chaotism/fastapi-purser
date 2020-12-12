from typing import NewType

from pydantic import UUID1

TransactionID = NewType("TransactionID", UUID1)
