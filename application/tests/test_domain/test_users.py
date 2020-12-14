from typing import Optional
from random import randint
from bson import ObjectId
from contextlib import contextmanager

import pytest
from pydantic import ValidationError

from domain.types import PDObjectId
from domain.errors import EntityError
from domain.users import UserID, User, UserService, UserRepository


class TestUserEnity:
    """
    tests with User fields validation
    """


class TestUserService:
    @pytest.fixture()
    def simple_user(self):
        return User(
            _id=ObjectId(),
            email='user_{}@localhost.com'.format(randint(1, 100)),
            name='user_{}'.format(randint(1, 100)),
        )

    @pytest.fixture()
    def fake_user_repo(self):

        class FakeUserRepository(UserRepository):
            data = {}

            def get_by_id(self, instance_id: UserID) -> Optional[User]:
                return self.data.get(instance_id)

            def insert(self, instance: User) -> UserID:
                instance.set_id(PDObjectId)
                self.data[instance.get_id()] = instance
                return instance.get_id()

            def update(self, instance: User) -> None:
                if instance.get_id():
                    self.data[instance.get_id()] = instance
                raise EntityError('Null id')

            def delete(self, instance: User) -> None:
                if instance.get_id():
                    self.data.pop(instance.get_id())
                raise EntityError('Null id')

            @contextmanager
            def atomic(self):
                try:
                    yield
                finally:
                    pass

        return FakeUserRepository()

    def test_register_user_positive(self, fake_user_repo, simple_user):
        user_service = UserService(fake_user_repo)
        new_user = user_service.register_user(email=simple_user.email, name=simple_user.name,)
        assert new_user.email == simple_user.email
        assert new_user.name == simple_user.name
        assert new_user == user_service.user_repo.get_by_id(new_user.id)

    @pytest.mark.parametrize(
        argnames="email,name",
        argvalues=[
            (None, 'Mario'),
            (1, 'Luigi'),
            ('cag;ca@cz', 'Bozer'),
        ],
        ids=['empty', 'int', 'wrong_email']
    )
    def test_register_user_negative(self, email, name, fake_user_repo):
        user_service = UserService(fake_user_repo)
        with pytest.raises(ValidationError) as err:
            new_user = user_service.register_user(email=email, name=name,)


class TestUserRepository:  # TODO: write test of base method of repos
    pass
