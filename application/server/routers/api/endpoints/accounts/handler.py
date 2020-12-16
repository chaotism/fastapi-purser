from typing import Any

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


@router.get('/{account_id}', response_model=StoredAccount)
async def get_account(
    account_id: AccountID,
    account_service: AccountService = Depends(get_account_service),
) -> Any:
    """
    Get a specific account by id.
    """
    account = await account_service.account_repo.get_by_id(instance_id=account_id)
    if not account:
        raise HTTPException(
            status_code=404,
            detail='Not found',
        )
    return account


@router.post('/', response_model=StoredAccount)
async def create_account(
    *,
    user_service: UserService = Depends(get_users_service),
    account_service: AccountService = Depends(get_account_service),
    account_in: AccountCreate,
) -> Any:
    """
    Create new account.
    """
    user = await user_service.user_repo.get_by_id(instance_id=account_in.owner_id)
    if not user:
        raise HTTPException(  # TODO: move checking into services
            status_code=400,
            detail='The user with this id is not exists in the system.',
        )
    existing_account = await account_service.account_repo.get_by_owner_id(owner_id=account_in.owner_id)
    if existing_account:
        raise HTTPException(  # TODO: move checking into services
            status_code=400,
            detail='The account with this owner_id is already exists in the system.',
        )
    balance = Money(amount=account_in.balance)
    account = await account_service.register_account(user, balance)
    return account


@router.post('/{account_id}/deposit', response_model=StoredAccount)
async def deposit(
    *,
    account_id: AccountID,
    account_service: AccountService = Depends(get_account_service),
    money_in: DepositMoney,
) -> Any:
    """
    Deposit money on account by id.
    """
    account = await account_service.account_repo.get_by_id(instance_id=account_id)
    if not account:
        raise HTTPException(  # TODO: move checking into services
            status_code=400,
            detail='The account with this id is not exists in the system.',
        )
    money = Money(amount=money_in.sum)
    await account_service.deposit(account, money)
    return await account_service.account_repo.get_by_id(instance_id=account_id)


@router.get('/{account_id}/transactions', response_model=StoredTransactions)
async def get_account_transactions(
    account_id: AccountID,
    account_service: AccountService = Depends(get_account_service),
    transaction_service: TransactionService = Depends(get_transaction_service),
) -> Any:
    """
    Get transaction of account by id.
    """
    account = await account_service.account_repo.get_by_id(instance_id=account_id)
    if not account:
        raise HTTPException(  # TODO: move checking into services
            status_code=400,
            detail='The account with this id is not exists in the system.',
        )
    transactions = await transaction_service.transaction_repo.get_many_by_account_id(account_id)  # TODO: add pagination
    return {'transactions': transactions}
