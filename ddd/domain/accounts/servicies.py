from dataclasses import dataclass
from datetime import datetime
from decimal import Decimal
from typing import Dict, List, Optional
from uuid import UUID

from .defines import CurrencyType
from .entities import Account, Money
from .repositories import AccountRepository
from .types import AccountID
from ..users.entities import User

from pydantic import BaseModel, EmailStr, UUID1


class AccountService:
    def __init__(self, account_repo: AccountRepository) -> None:
        self.account_repo = account_repo

    def register_account(self, account_id: AccountID, user: User, balance: Money) -> Account:
        account = Account(_id=account_id, owner=user, balance=balance)  # TODO: create id after save
        self.account_repo.insert(account)
        return account

    def deposit(self, account: Account, money: Money):
        account.balance.amount += money.amount
        self.account_repo.update(account)

    def withdraw(self, account: Account, money: Money):
        account.balance.amount -= money.amount
        self.account_repo.update(account)
