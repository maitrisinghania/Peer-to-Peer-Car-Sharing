
from pydantic import BaseModel
from datetime import date, datetime
from typing import Optional

class CarBase(BaseModel):
    make: str
    model: str
    year: int
    type: str
    color: str
    seats: int
    price_per_day: float
    location: str
    description: Optional[str] = None
    available_from: Optional[date] = None
    available_to: Optional[date] = None

class CarCreate(CarBase):
    image_url: str

class CarUpdate(BaseModel):
    make: Optional[str] = None
    model: Optional[str] = None
    year: Optional[int] = None
    type: Optional[str] = None
    color: Optional[str] = None
    seats: Optional[int] = None
    price_per_day: Optional[float] = None
    location: Optional[str] = None
    description: Optional[str] = None
    available_from: Optional[date] = None
    available_to: Optional[date] = None
    image_url: Optional[str] = None

class CarResponse(CarBase):
    id: str
    owner_id: str
    image_url: str
    created_at: datetime

    class Config:
        orm_mode = True
