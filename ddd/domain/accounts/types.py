from typing import NewType

from pydantic import UUID1


AccountID = NewType("AccountID", UUID1)
