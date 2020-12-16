from enum import Enum


class StatusType(Enum):  # TODO: add checking new==>success or failed
    new = 'new'
    success = 'success'   # TODO: add encoder to json
    failed = 'failed'
