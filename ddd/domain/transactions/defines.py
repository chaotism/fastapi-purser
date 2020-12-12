from enum import Enum


class StatusType(Enum):  # TODO: add checking new==>success or failed
    new = "new"
    success = "success"
    failed = "failed"
