from dataclasses import dataclass
from datetime import datetime
from decimal import Decimal
from typing import Dict, List, Optional
from uuid import UUID

from .defines import CurrencyType
from ..users.entities import User

from pydantic import BaseModel, EmailStr, UUID1


class Cash(BaseModel):
    amount: Decimal
    currency: CurrencyType


class Account(BaseModel):
    id: UUID1
    owner: User

    balance: Cash


