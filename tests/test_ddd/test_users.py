from typing import Optional
from random import randint
from uuid import uuid1
import pytest
from ddd.domain.users import UserID, User, UserService, UserRepository


class FakeUserRepository(UserRepository):
    data = {}

    def get_by_id(self, instance_id: UserID) -> Optional[User]:
        return self.data.get(instance_id)

    def insert(self, instance: User) -> None:
        self.data[User._id] = User


class TestUserService:
    @pytest.fixture()
    def user_repo(self):
        return FakeUserRepository()

    @pytest.fixture()
    def simple_user(self):
        return User(
            _id=uuid1(),
            email='user_{}@localhost.com'.format(randint(1, 100)),
            name='user_{}'.format(randint(1, 100)),
        )

    def test_simple_positive_scenario(self, user_repo, simple_user):
        user_service = UserService(user_repo)
        user = user_service.register_user(user_id=simple_user._id, email=simple_user.email, name=simple_user.name,)
        assert user.dict() == simple_user.dict()
        assert user == user_service.user_repo.get_by_id(simple_user._id)


class TestUserRepository:  # TODO: write test of base method of repos
    pass
