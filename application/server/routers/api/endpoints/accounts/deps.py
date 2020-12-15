from typing import Generator

from domain.accounts import AccountService, MotorAccountRepository


def get_account_service() -> Generator:
    yield AccountService(MotorAccountRepository())  # TODO: add excepting error and connection close
