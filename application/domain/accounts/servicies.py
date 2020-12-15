from ..errors import EntityError
from ..types import Service
from ..users import User
from .entities import Account, Money
from .repositories import AccountRepository


class AccountService(Service):
    def __init__(self, account_repo: AccountRepository) -> None:
        self.account_repo = account_repo

    def register_account(self, user: User, balance: Money) -> Account:
        account = Account(owner=user, balance=balance)
        repo_account_id = self.account_repo.insert(account)
        return self.account_repo.get_by_id(repo_account_id)

    def deposit(self, account: Account, money: Money):
        if not account.id:
            raise EntityError('Null id')
        if not self.account_repo.get_by_id(account.id):
            raise EntityError('Not exists')
        account.balance.amount += money.amount
        self.account_repo.update(account)

    def withdraw(self, account: Account, money: Money):
        if not account.id:
            raise EntityError('Null id')
        if not self.account_repo.get_by_id(account.id):
            raise EntityError('Not exists')
        account.balance.amount -= money.amount
        self.account_repo.update(account)
