from typing import Optional
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from pydantic import BaseModel

Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True, nullable=True)
    email = Column(String, unique=True, index=True, nullable=True)
    hashed_password = Column(String, nullable=True)
    full_name = Column(String, nullable=True)
    is_active = Column(Integer, nullable=True)

    def update_data(self, user: "User") -> None:
        self.username = user.username
        self.email = user.email
        self.hashed_password = user.hashed_password
        self.full_name = user.full_name
        self.is_active = user.is_active

class ExceptionClass(BaseModel):
    detail: str