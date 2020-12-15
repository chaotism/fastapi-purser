from typing import Generator

from domain.transactions import TransactionService, MotorTransactionRepository


def get_transaction_service() -> Generator:
    yield TransactionService(MotorTransactionRepository())  # TODO: add excepting error and connection close
