from dataclasses import dataclass
from datetime import datetime
from decimal import Decimal
from typing import Dict, List, Optional
from uuid import UUID

from .types import UserName


from pydantic import BaseModel, EmailStr, UUID1


class User(BaseModel):
    _id: UUID1
    email: EmailStr
    name: Optional[UserName] = None
