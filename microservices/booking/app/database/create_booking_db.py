from sqlalchemy.orm import Session
from ..config.db_config import engine
from ..models.booking import Booking

class CreateBookingDB:
    @staticmethod
    def add_booking(booking: Booking) -> Booking:
        with Session(engine) as session:
            session.add(booking)
            session.commit()
            session.refresh(booking)
            return booking