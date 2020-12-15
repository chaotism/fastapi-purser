from typing import List

from loguru import logger

from ..types import Service
from ..errors import EntityError
from ..accounts import AccountID, Account, AccountService
from .entities import Transaction, Money
from .repositories import TransactionRepository
from .types import TransactionID


class TransactionService(Service):
    def __init__(self, transaction_repo: TransactionRepository) -> None:
        self.transaction_repo = transaction_repo

    def register_transaction(self, from_account: Account, to_account: Account, amount: Money) -> Transaction:
        transaction = Transaction(from_account=from_account, to_account=to_account, sum=amount)
        repo_transaction_id = self.transaction_repo.insert(transaction)
        return self.transaction_repo.get_by_id(repo_transaction_id)

    def evaluate_transaction(self, account_service: AccountService, transaction: Transaction) -> Transaction:
        if not transaction.id:
            raise EntityError('Null id')
        if not self.transaction_repo.get_by_id(Transaction.id):
            raise EntityError('Not exists')
        try:
            with account_service.account_repo.atomic():
                account_service.withdraw(transaction.from_account, transaction.sum)
                account_service.deposit(transaction.to_account, transaction.sum)
                transaction.set_complete()
                self.transaction_repo.update(transaction)
        except Exception as err:
            logger.error(str(err))  # TODO: use logger
            transaction.set_failed(str(err))
            self.transaction_repo.update(transaction)
        return transaction

    def get_account_transaction(self, account_id: AccountID) -> List[Transaction]:
        transactions = self.transaction_repo.get_by_account_id(account_id)
        return transactions
