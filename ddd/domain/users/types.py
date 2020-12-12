from typing import NewType

from pydantic import UUID1

UserID = NewType("UserID", UUID1)
UserName = NewType("UserName", str)
