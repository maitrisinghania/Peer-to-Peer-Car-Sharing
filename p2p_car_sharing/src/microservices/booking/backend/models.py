
from pydantic import BaseModel
from datetime import date, datetime
from typing import Optional

class BookingBase(BaseModel):
    car_id: str
    renter_id: str
    start_date: date
    end_date: date
    total_price: float

class BookingCreate(BookingBase):
    pass

class BookingUpdate(BaseModel):
    status: Optional[str] = None
    start_date: Optional[date] = None
    end_date: Optional[date] = None

class BookingResponse(BookingBase):
    id: str
    status: str
    created_at: datetime

    class Config:
        orm_mode = True
