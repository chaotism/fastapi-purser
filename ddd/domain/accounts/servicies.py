from dataclasses import dataclass
from datetime import datetime
from decimal import Decimal
from typing import Dict, List, Optional
from uuid import UUID

from .defines import CurrencyType
from .entities import Account
from .repositories import AccountRepository
from .types import AccountID
from ..users.entities import User

from pydantic import BaseModel, EmailStr, UUID1


class AccountService:
    def __init__(self) -> None:
        self.account_repo = AccountRepository()

    def register_account(self, account_id: AccountID) -> Account:
        clan = self._get_clan(account_id)
        nickname = self._get_nickname(account_id)
        if self._is_account_banned(account_id):
            raise Exception('Account can not be created.')
        account = Account(account_id, nickname, clan)
        self.account_repo.insert(account)
        return account
