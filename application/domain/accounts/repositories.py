from abc import ABCMeta, abstractmethod
from contextlib import contextmanager, asynccontextmanager
from typing import Optional

from dbs.mongo import client, database as motor_database
from ..errors import EntityError
from ..types import Repository
from ..users.types import UserID
from .entities import Account
from .types import AccountID


class AccountRepository(Repository):
    __metaclass__ = ABCMeta

    @abstractmethod
    async def get_count(self) -> int:
        pass

    @abstractmethod
    async def get_by_id(self, instance_id: AccountID) -> Optional[Account]:
        pass

    @abstractmethod
    async def insert(self, instance: Account) -> None:
        pass

    @abstractmethod
    async def update(self, instance: Account) -> None:
        pass

    @abstractmethod
    async def delete(self, instance: Account) -> None:
        pass

    @contextmanager
    async def atomic(self):
        pass


class MotorAccountRepository(AccountRepository):
    collection = motor_database.accounts

    async def get_count(self) -> int:
        return self.collection.count_documents({})

    async def get_by_id(self, instance_id: AccountID) -> Optional[Account]:
        account = await self.collection.find_one({'_id': instance_id})
        if account is None:
            return
        return Account(**account)

    async def get_by_owner_id(self, owner_id: UserID) -> Optional[Account]:
        account = await self.collection.find_one({'owner._id': owner_id})
        if account is None:
            return
        return Account(**account)

    async def insert(self, instance: Account) -> AccountID:
        data = instance.dict(by_alias=True)
        data.pop('_id')
        result = await self.collection.insert_one(data)
        return result.inserted_id

    async def update(self, instance: Account) -> None:
        instance_id = instance.get_id()
        if not instance_id:
            raise EntityError('Null id')
        data = instance.dict(by_alias=True)
        data.pop('_id')
        await self.collection.update_one({'_id': instance_id}, {'$set': data})

    async def delete(self, instance: Account) -> None:
        instance_id = instance.get_id()
        if not instance_id:
            raise EntityError('Null id')
        await self.collection.delete_one({'_id': instance_id})

    @asynccontextmanager
    async def atomic(self):
        async with await client.start_session() as s:
            async with s.start_transaction():
                yield
