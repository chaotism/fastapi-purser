from abc import ABCMeta, abstractmethod
from contextlib import contextmanager, asynccontextmanager
from typing import Optional

from dbs.mongo import client, database as motor_database
from .entities import Account
from .types import AccountID
from ..errors import EntityError
from ..types import Repository


class AccountRepository(Repository):
    __metaclass__ = ABCMeta

    @abstractmethod
    def get_by_id(self, instance_id: AccountID) -> Optional[Account]:
        pass

    @abstractmethod
    def insert(self, instance: Account) -> None:
        pass

    @abstractmethod
    def update(self, instance: Account) -> None:
        pass

    @abstractmethod
    def delete(self, instance: Account) -> None:
        pass

    @abstractmethod
    @contextmanager
    def atomic(self):
        pass


class MotorAccountRepository(AccountRepository):
    collection = motor_database.transactions

    async def get_by_id(self, instance_id: AccountID) -> Optional[Account]:
        transaction = await self.collection.find_one({'_id': instance_id})
        return Account(**transaction)

    async def insert(self, instance: Account) -> AccountID:
        data = instance.dict(by_alias=True)
        result = await self.collection.insert_one(data)
        return result.inserted_id

    async def update(self, instance: Account) -> None:
        instance_id = instance.get_id()
        if instance_id:
            data = instance.dict(by_alias=True)
            data.pop('_id')
            await self.collection.update_one({'_id': instance_id}, {'$set': data})
        raise EntityError('Null id')

    async def delete(self, instance: Account) -> None:
        instance_id = instance.get_id()
        if instance_id:
            await self.collection.delete_one({'_id': instance_id})
        raise EntityError('Null id')

    @asynccontextmanager
    async def atomic(self):
        async with await client.start_session() as s:
            async with s.start_transaction():
                yield
