from typing import NewType

from ...types import PDObjectId

UserID = NewType("UserID", PDObjectId)
UserName = NewType("UserName", str)
