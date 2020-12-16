from abc import ABCMeta, abstractmethod
from contextlib import contextmanager, asynccontextmanager
from typing import List, Optional

from dbs.mongo import client, database as motor_database
from ..errors import EntityError
from ..types import Repository
from ..accounts import AccountID

from .entities import Transaction
from .types import TransactionID


class TransactionRepository(Repository):
    __metaclass__ = ABCMeta

    @abstractmethod
    async def get_count(self) -> int:
        pass

    @abstractmethod
    async def get_by_id(self, instance_id: TransactionID) -> Optional[Transaction]:
        pass

    @abstractmethod
    async def get_many_by_account_id(self, account_id: AccountID) -> Optional[List[Transaction]]:
        pass

    @abstractmethod
    async def insert(self, instance: Transaction) -> None:
        pass

    @abstractmethod
    async def update(self, instance: Transaction) -> None:
        pass

    @abstractmethod
    async def delete(self, instance: Transaction) -> None:
        pass

    @abstractmethod
    @contextmanager
    async def atomic(self):
        pass


class MotorTransactionRepository(TransactionRepository):
    collection = motor_database.transactions

    async def get_count(self) -> int:
        return self.collection.count_documents({})

    async def get_by_id(self, instance_id: TransactionID) -> Optional[Transaction]:
        transaction = await self.collection.find_one({'_id': instance_id})
        if transaction is None:
            return
        return Transaction(**transaction)

    async def get_many_by_account_id(
        self, account_id: AccountID, buff_size: int = 1000
    ) -> Optional[List[Transaction]]:
        transactions_data_cursor = self.collection.find(
            {'$or': [{'from_account._id': account_id}, {'to_account._id': account_id}]}
        )
        transactions_data = [
            data for data in await transactions_data_cursor.to_list(length=buff_size)
        ]
        if transactions_data is None:
            return
        return list(
            map(lambda transaction: Transaction(**transaction), transactions_data)
        )

    async def insert(self, instance: Transaction) -> TransactionID:
        data = instance.dict(by_alias=True)
        data.pop('_id')
        result = await self.collection.insert_one(data)
        return result.inserted_id

    async def update(self, instance: Transaction) -> None:
        instance_id = instance.get_id()
        if not instance_id:
            raise EntityError('Null id')
        data = instance.dict(by_alias=True)
        data.pop('_id')
        await self.collection.update_one({'_id': instance_id}, {'$set': data})

    async def delete(self, instance: Transaction) -> None:
        instance_id = instance.get_id()
        if not instance_id:
            raise EntityError('Null id')
        await self.collection.delete_one({'_id': instance_id})

    @asynccontextmanager
    async def atomic(self):
        async with await client.start_session() as s:
            async with s.start_transaction():
                yield
