from typing import Any, Dict, Generic, List, Optional, Type, TypeVar, Union

from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel


class CRUDBase:
    def __init__(self, model: dict):
        """
        CRUD object with default methods to Create, Read, Update, Delete (CRUD).

        **Parameters**

        * `model`: A model class
        """
        self.model = model

    def get(self, obj_id: int) -> Optional[Dict[str, Any]]:
        obj = self.model.get(obj_id)
        return obj

    def get_multi(self,  *, skip: int = 0, limit: int = 100) -> List[Dict[str, Any]]:
        return list(self.model.values())[skip:limit]  # TODO: will not work

    def create(self, *, obj_in: dict) -> dict:
        max_id = max(list(self.model.keys()))
        self.model[max_id+1] = obj_in
        return obj_in

    def update(self, *, obj_id: int, obj_in: Union[Dict[str, Any]]) -> Dict[str, Any]:
        self.model[obj_id] = obj_in
        return obj_in

    def remove(self, *, obj_id: int) -> Optional[Dict[str, Any]]:
        obj = self.model.pop(obj_id, None)
        return obj
