from loguru import logger

from .defines import StatusType
from .entities import Transaction, Money
from .repositories import TransactionRepository
from .types import TransactionID
from .defines import StatusType
from ..accounts.servicies import AccountService
from ..accounts.entities import Account
from ..types import Service
from ..errors import EntityError


class TransactionService(Service):
    def __init__(self, transaction_repo: TransactionRepository) -> None:
        self.transaction_repo = transaction_repo

    def register_transaction(self, from_account: Account, to_account: Account, amount: Money) -> Transaction:
        transaction = Transaction(from_account=from_account, to_account=to_account, sum=amount)
        repo_transaction_id = self.transaction_repo.insert(transaction)
        return self.transaction_repo.get_by_id(repo_transaction_id)

    def evaluate_transaction(self, account_service: AccountService, transaction_id: TransactionID) -> Transaction:
        transaction = self.transaction_repo.get_by_id(transaction_id)
        if not transaction:
            raise EntityError('Not exists transaction')
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
