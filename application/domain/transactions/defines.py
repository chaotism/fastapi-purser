from enum import Enum


class StatusType(Enum):  # TODO: add checking new==>success or failed   # TODO: add encoder to json
    new = 'new'
    success = 'success'
    failed = 'failed'
