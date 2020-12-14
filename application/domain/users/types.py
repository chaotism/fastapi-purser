from typing import NewType

from ...domain.types import PDObjectId

UserID = NewType('UserID', PDObjectId)
UserName = NewType('UserName', str)
