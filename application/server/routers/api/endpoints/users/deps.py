from domain.users import UserService, MotorUserRepository


def get_users_service() -> UserService:
    return UserService(
        MotorUserRepository()
    )  # TODO: add excepting error and connection close
