from ..errors import EntityError
from ..types import Service
from ..users import User
from .entities import Account, Money
from .repositories import AccountRepository


class AccountService(Service):
    def __init__(self, account_repo: AccountRepository) -> None:
        self.account_repo = account_repo

    async def register_account(self, user: User, balance: Money) -> Account:
        account = Account(owner=user, balance=balance)
        async with self.account_repo.atomic():
            repo_account_id = await self.account_repo.insert(account)
            return await self.account_repo.get_by_id(repo_account_id)

    async def deposit(self, account: Account, money: Money):
        if not account.get_id():
            raise EntityError('Null id')
        if not self.account_repo.get_by_id(account.get_id()):
            raise EntityError('Not exists')
        account.balance.amount += money.amount
        await self.account_repo.update(account)

    async def withdraw(self, account: Account, money: Money):
        if not account.get_id():
            raise EntityError('Null id')
        if not self.account_repo.get_by_id(account.get_id()):
            raise EntityError('Not exists')
        account.balance.amount -= money.amount
        await self.account_repo.update(account)
