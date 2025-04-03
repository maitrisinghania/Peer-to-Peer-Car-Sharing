from typing import List
from pydantic import BaseModel, EmailStr

class UserCreate(BaseModel):
    email: EmailStr
    name: str
    password: str
    role: str

class UserUpdate(BaseModel):
    name: str = None
    password: str = None

class UserValidators:
    @staticmethod
    def add_validator(user: UserCreate):
        # Add validation logic here if needed
        return user

    @staticmethod
    def list_id_validator(users: List[UserUpdate]):
        # Add validation logic here if needed
        return users

    @staticmethod
    def id_validator(user: UserUpdate):
        # Add validation logic here if needed
        return user

    @staticmethod
    def rollback_validator(user: UserUpdate):
        # Add validation logic here if needed
        return user