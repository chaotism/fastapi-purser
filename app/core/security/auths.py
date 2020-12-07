"""API Authentications"""  # TODO: not implement


def get_password_hash(password: str) -> int:
    return hash(password)  # TODO: naive


def verify_password(password: str, hashed_password: int) -> bool:
    return get_password_hash(password) == hashed_password
