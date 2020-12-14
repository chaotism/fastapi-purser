from typing import List

from ..errors import EntityError
from ..transactions import Transaction
from ..transactions import TransactionService
from ..types import Service
from ..users import User
from .entities import Account
from .entities import Money
from .repositories import AccountRepository
from .types import AccountID


class AccountService(Service):
    def __init__(self, account_repo: AccountRepository) -> None:
        self.account_repo = account_repo

    def register_account(
        self, account_id: AccountID, user: User, balance: Money
    ) -> Account:
        account = Account(
            _id=account_id, owner=user, balance=balance
        )  # TODO: create id after save
        self.account_repo.insert(account)
        return account

    def deposit(self, account: Account, money: Money):
        account.balance.amount += money.amount
        self.account_repo.update(account)

    def withdraw(self, account: Account, money: Money):
        account.balance.amount -= money.amount
        self.account_repo.update(account)

    @staticmethod
    def get_account_transactions(
        transaction_service: TransactionService, account_id: AccountID
    ) -> List[Transaction]:
        transactions = transaction_service.transaction_repo.get_by_account_id(
            account_id
        )
        return transactions

    @staticmethod
    def is_account_owner(account: Account, current_user: User) -> bool:
        if account.owner.id is None:
            raise EntityError("account owner haven't id'")
        if current_user.id is None:
            raise EntityError("checking_user haven't id'")
        return account.owner.id == current_user.id
