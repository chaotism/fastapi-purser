from typing import Optional

from pydantic import BaseModel, EmailStr

from domain.users import User


# Properties to receive on user creation
class UserCreate(BaseModel):
    email: EmailStr
    name: Optional[str] = None
    is_super_user: Optional[bool] = False


# Properties to return to client
class StoredUser(User):
    pass
