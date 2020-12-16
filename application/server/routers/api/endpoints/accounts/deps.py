from domain.accounts import AccountService, MotorAccountRepository


def get_account_service() -> AccountService:
    return AccountService(
        MotorAccountRepository()
    )  # TODO: add excepting error and connection close
