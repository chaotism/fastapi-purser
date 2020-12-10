from dataclasses import dataclass
from datetime import datetime
from decimal import Decimal
from typing import Dict, List, Optional
from uuid import UUID

from .defines import StatusType
from ..accounts.entities import Account, Cash


from pydantic import BaseModel, EmailStr, UUID1


# TODO: use pydantic types

class Transaction(BaseModel):
    id: UUID1

    from_account: Account
    to_account: Account

    value: Cash

    status: StatusType
