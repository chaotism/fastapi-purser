from .entities import Account, Money
from .repositories import AccountRepository
from .types import AccountID
from ..users.entities import User
from ...domain.types import Service


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
