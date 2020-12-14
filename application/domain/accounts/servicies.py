from typing import List
from .entities import Account, Money
from .repositories import AccountRepository
from .types import AccountID
from ..users import User
from ..transactions import Transaction, TransactionService
from ..types import Service
from ..errors import EntityError


class AccountService(Service):
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

    @staticmethod
    def get_account_transactions(transaction_service: TransactionService, account_id: AccountID) -> List[Transaction]:
        transactions = transaction_service.transaction_repo.get_by_account_id(account_id)
        return transactions

    @staticmethod
    def get_account_transactions(transaction_service: TransactionService, account_id: AccountID) -> List[Transaction]:
        transactions = transaction_service.transaction_repo.get_by_account_id(account_id)
        return transactions

    @staticmethod
    def is_account_owner(account: Account, checking_user: User) -> bool:
        if account.owner.id is None:
            raise EntityError("account owner haven't id'")
        if checking_user.id is None:
            raise EntityError("checking_user haven't id'")
        return account.owner.id == checking_user.id
