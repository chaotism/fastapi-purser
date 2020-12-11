from dataclasses import dataclass
from datetime import datetime
from decimal import Decimal
from typing import Dict, List, Optional
from uuid import UUID

from .defines import CurrencyType
from .types import AccountID
from ..users.entities import User
from ...types import Entity

from pydantic import BaseModel, EmailStr, UUID1


class Money(Entity):
    amount: Decimal
    currency: CurrencyType


class Account(Entity):
    _id: AccountID
    owner: User

    balance: Money
