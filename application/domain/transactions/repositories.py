from abc import ABCMeta, abstractmethod
from contextlib import contextmanager, asynccontextmanager
from typing import List, Optional

from .entities import Transaction
from .types import TransactionID
from ..errors import EntityError
from ..types import Repository


from dbs.mongo import client, database as motor_database


class TransactionRepository(Repository):
    __metaclass__ = ABCMeta

    @abstractmethod
    def get_by_id(self, instance_id: TransactionID) -> Optional[Transaction]:
        pass

    @abstractmethod
    def get_by_account_id(self, account_id: TransactionID) -> Optional[List[Transaction]]:
        pass

    @abstractmethod
    def insert(self, instance: Transaction) -> None:
        pass

    @abstractmethod
    def update(self, instance: Transaction) -> None:
        pass

    @abstractmethod
    def delete(self, instance: Transaction) -> None:
        pass

    @abstractmethod
    @contextmanager
    def atomic(self):
        pass


class MotorTransactionRepository(TransactionRepository):
    collection = motor_database.transactions

    async def get_by_id(self, instance_id: TransactionID) -> Optional[Transaction]:
        transaction = await self.collection.find_one({'_id': instance_id})
        return Transaction(**transaction)

    async def insert(self, instance: Transaction) -> TransactionID:
        data = instance.dict(by_alias=True)
        result = await self.collection.insert_one(data)
        return result.inserted_id

    async def update(self, instance: Transaction) -> None:
        instance_id = instance.get_id()
        if instance_id:
            data = instance.dict(by_alias=True)
            data.pop('_id')
            result = await self.collection.update_one({'_id': instance_id}, {'$set': data})
        raise EntityError('Null id')

    async def delete(self, instance: Transaction) -> None:
        instance_id = instance.get_id()
        if instance_id:
            await self.collection.delete_one({'_id': instance_id})
        raise EntityError('Null id')

    @asynccontextmanager
    async def atomic(self):
        async with await client.start_session() as s:
            async with s.start_transaction():
                yield
