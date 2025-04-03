from sqlalchemy.orm import Session
from ..config.db_config import engine
from ..models.booking import Booking

class ReadBookingDB:
    @staticmethod
    def get_booking(booking_id: int) -> Booking:
        with Session(engine) as session:
            booking = session.get(Booking, booking_id)
            return booking