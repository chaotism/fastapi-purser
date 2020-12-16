from abc import ABCMeta, abstractmethod
from contextlib import contextmanager, asynccontextmanager
from typing import Optional

from pydantic import EmailStr

from dbs.mongo import client, database as motor_database

from ..errors import EntityError
from ..types import Repository
from .entities import User
from .types import UserID


class UserRepository(Repository):
    __metaclass__ = ABCMeta

    @abstractmethod
    async def get_count(self) -> int:
        pass

    @abstractmethod
    async def get_by_id(self, instance_id: UserID) -> Optional[User]:
        pass

    @abstractmethod
    async def get_by_email(self, email: EmailStr) -> Optional[User]:
        pass

    @abstractmethod
    async def insert(self, instance: User) -> UserID:
        pass

    @abstractmethod
    async def update(self, instance: User) -> None:
        pass

    @abstractmethod
    async def delete(self, instance: User) -> None:
        pass

    @abstractmethod
    @contextmanager
    async def atomic(self):
        pass


class MotorUserRepository(UserRepository):
    collection = motor_database.users

    async def get_count(self) -> int:
        return self.collection.count_documents({})

    async def get_by_id(self, instance_id: UserID) -> Optional[User]:
        user = await self.collection.find_one({'_id': instance_id})
        if user is None:
            return
        return User(**user)

    async def get_by_email(self, email: EmailStr) -> Optional[User]:
        user = await self.collection.find_one({'email': email})
        if user is None:
            return
        return User(**user)

    async def insert(self, instance: User) -> UserID:
        data = instance.dict(by_alias=True)
        data.pop('_id')
        result = await self.collection.insert_one(data)
        return result.inserted_id

    async def update(self, instance: User) -> None:
        instance_id = instance.get_id()
        if not instance_id:
            raise EntityError('Null id')
        data = instance.dict(by_alias=True)
        data.pop('_id')
        await self.collection.update_one({'_id': instance_id}, {'$set': data})

    async def delete(self, instance: User) -> None:
        instance_id = instance.get_id()
        if not instance_id:
            raise EntityError('Null id')
        await self.collection.delete_one({'_id': instance_id})

    @asynccontextmanager
    async def atomic(self):
        async with await client.start_session() as s:
            async with s.start_transaction():
                yield
