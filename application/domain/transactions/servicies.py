from loguru import logger

from .defines import StatusType
from .entities import Transaction, Money
from .repositories import TransactionRepository
from .types import TransactionID
from ..accounts.servicies import  AccountService
from ..accounts.entities import Account
from ..types import Service


class TransactionService(Service):
    def __init__(self, transaction_repo: TransactionRepository) -> None:
        self.transaction_repo = transaction_repo

    def register_transaction(self, from_account: Account, to_account: Account, sum: Money) -> Transaction:
        transaction = Transaction(from_account=from_account, to_account=to_account, sum=sum)
        repo_transaction_id = self.transaction_repo.insert(transaction)
        return self.transaction_repo.get_by_id(repo_transaction_id)

    def evaluate_transaction(self, account_service: AccountService, transaction_id: TransactionID) -> StatusType:
        transaction = self.transaction_repo.get_by_id(transaction_id)
        try:
            with account_service.account_repo.atomic():
                account_service.withdraw(transaction.from_account, transaction.sum)
                account_service.deposit(transaction.to_account, transaction.sum)
        except Exception as err:
            logger.error(err)  # TODO: use logger
            return StatusType(StatusType.failed)
        return StatusType(StatusType.success)
