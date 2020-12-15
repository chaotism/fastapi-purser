from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException

from domain.accounts import AccountService, AccountID, Money
from domain.users import UserService
from domain.transactions import TransactionService
from .deps import get_account_service
from .schemas import AccountCreate, StoredAccount, DepositMoney, StoredTransactions
from ..users.deps import get_users_service
from ..transactions.deps import get_transaction_service

router = APIRouter()


# TODO: add checking current user


@router.post('/', response_model=StoredAccount)
def create_account(
    *,
    user_service: UserService = Depends(get_users_service),
    account_service: AccountService = Depends(get_account_service),
    account_in: AccountCreate,
) -> Any:
    """
    Create new account.
    """
    user = user_service.user_repo.get_by_id(instance_id=account_in.owner_id)
    if not user:
        raise HTTPException(
            status_code=400,
            detail='The user with this id is not exists in the system.',
        )
    balance = Money(amount=account_in.balance)
    account = account_service.register_account(user, balance)
    return account


@router.get('/{account_id}', response_model=StoredAccount)
def read_account_by_id(
    account_id: AccountID,
    account_service: AccountService = Depends(get_account_service),
) -> Any:
    """
    Get a specific account by id.
    """
    account = account_service.account_repo.get_by_id(instance_id=account_id)
    if not account:
        raise HTTPException(
            status_code=404,
            detail='Not found',
        )
    return account


@router.post('/{account_id}/deposit', response_model=StoredAccount)
def deposit_on_account_by_id(
    *,
    account_id: AccountID,
    account_service: AccountService = Depends(get_account_service),
    money_in: DepositMoney,
) -> Any:
    """
    Deposit money on account by id.
    """
    account = account_service.account_repo.get_by_id(instance_id=account_id)
    if not account:
        raise HTTPException(
            status_code=400,
            detail='The account with this id is not exists in the system.',
        )
    deposit_money = Money(amount=money_in.sum)
    account_service.deposit(account, deposit_money)
    return account_service.account_repo.get_by_id(instance_id=account_id)


@router.get('/{account_id}/transaction', response_model=StoredTransactions)
def read_account_transaction_by_id(
    account_id: AccountID,
    account_service: AccountService = Depends(get_account_service),
    transaction_service: TransactionService = Depends(get_transaction_service),
) -> Any:
    """
    Get transaction of account by id.
    """
    account = account_service.account_repo.get_by_id(instance_id=account_id)
    if not account:
        raise HTTPException(
            status_code=400,
            detail='The account with this id is not exists in the system.',
        )
    transactions = account_service.get_account_transactions(transaction_service, account.id)
    return {'transactions': transactions}
