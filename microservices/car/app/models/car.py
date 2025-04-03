from typing import Optional
from sqlalchemy import Column, Integer, String, Date, CheckConstraint
from sqlalchemy.ext.declarative import declarative_base
from pydantic import BaseModel

Base = declarative_base()

class Car(Base):
    __tablename__ = "cars"
    id = Column(Integer, primary_key=True, index=True)
    owner_id = Column(Integer, nullable=True)
    make = Column(String(50), nullable=True)
    model = Column(String(50), nullable=True)
    year = Column(Integer, nullable=True)
    description = Column(String, nullable=True)
    price_per_day = Column(Integer, nullable=True)
    available_from = Column(Date, nullable=True)
    available_until = Column(Date, nullable=True)
    status = Column(String(20), CheckConstraint("status IN ('Available', 'Unavailable')"), nullable=True)

    def update_data(self, car: "Car") -> None:
        self.owner_id = car.owner_id
        self.make = car.make
        self.model = car.model
        self.year = car.year
        self.description = car.description
        self.price_per_day = car.price_per_day
        self.available_from = car.available_from
        self.available_until = car.available_until
        self.status = car.status

class ExceptionClass(BaseModel):
    detail: str