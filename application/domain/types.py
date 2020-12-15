from datetime import datetime
from bson import ObjectId
from typing import Optional
from pydantic import BaseModel, Field


class PDObjectId(ObjectId):

    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        if not ObjectId.is_valid(v):
            raise ValueError('Invalid ObjectId')
        return ObjectId(v)

    @classmethod
    def __modify_schema__(cls, field_schema):
        field_schema.update(type='string')


class Entity(BaseModel):
    id: Optional[PDObjectId] = Field(alias='_id')
    created_at: Optional[datetime] = Field(default_factory=lambda v: datetime.now())

    def get_id(self):
        return self.id

    def set_id(self, id: PDObjectId):
        self.id = id

    def dict(self, *args, **kwargs):
        hidden_fields = set(
            attribute_name
            for attribute_name, model_field in self.__fields__.items()
            if model_field.field_info.extra.get("hidden") is True
        )
        kwargs.setdefault("exclude", hidden_fields)
        return super().dict(*args, **kwargs)

    class Config:
        arbitrary_types_allowed = True
        json_encoders = {
            ObjectId: str
        }


class DAO:
    pass


class Service:
    pass


class Repository:
    pass
