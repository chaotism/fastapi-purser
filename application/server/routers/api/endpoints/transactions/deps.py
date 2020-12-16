from domain.transactions import TransactionService, MotorTransactionRepository


def get_transaction_service() -> TransactionService:
    return TransactionService(
        MotorTransactionRepository()
    )  # TODO: add excepting error and connection close
