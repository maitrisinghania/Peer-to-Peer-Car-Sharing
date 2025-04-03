from typing import Optional
from sqlalchemy import Column, Integer, String, Date, CheckConstraint
from sqlalchemy.ext.declarative import declarative_base
from pydantic import BaseModel

Base = declarative_base()

class Booking(Base):
    __tablename__ = "bookings"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, nullable=True)
    car_id = Column(Integer, nullable=True)
    start_date = Column(Date, nullable=True)
    end_date = Column(Date, nullable=True)
    status = Column(String(20), CheckConstraint("status IN ('Pending', 'Confirmed', 'Cancelled')"), nullable=True)

    def update_data(self, booking: "Booking") -> None:
        self.user_id = booking.user_id
        self.car_id = booking.car_id
        self.start_date = booking.start_date
        self.end_date = booking.end_date
        self.status = booking.status

class ExceptionClass(BaseModel):
    detail: str