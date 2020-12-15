from typing import Generator

from domain.users import UserService, MotorUserRepository


def get_users_service() -> Generator:
    yield UserService(MotorUserRepository())  # TODO: add excepting error and connection close
