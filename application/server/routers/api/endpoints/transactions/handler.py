from typing import Any

from fastapi import APIRouter, Depends, HTTPException

from domain.types import PDObjectId
from domain.accounts import AccountService, Money
from domain.transactions import TransactionService, Transaction
from .deps import get_transaction_service
from .schemas import TransactionCreate, StoredTransaction
from ..accounts.deps import get_account_service

router = APIRouter()


# TODO: add checking current user


@router.post('/', response_model=StoredTransaction)
def create_transaction(
    *,
    account_service: AccountService = Depends(get_account_service),
    transaction_service: TransactionService = Depends(get_transaction_service),
    transaction_in: TransactionCreate,
) -> Any:
    """
    Create new transaction.
    """
    from_account = account_service.account_repo.get_by_id(instance_id=transaction_in.from_account_id)
    to_account = account_service.account_repo.get_by_id(instance_id=transaction_in.to_account_id)
    if not (from_account and to_account):
        raise HTTPException(
            status_code=400,
            detail='One of more account used in transcation is not exists in the system.',
        )
    transaction_amount = Money(amount=transaction_in.sum)

    transaction = transaction_service.register_transaction(from_account, to_account, transaction_amount)
    return transaction
