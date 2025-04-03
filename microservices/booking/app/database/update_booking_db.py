from sqlalchemy.orm import Session
from ..config.db_config import engine
from ..models.booking import Booking

class UpdateBookingDB:
    @staticmethod
    def update_booking(booking: Booking) -> Booking:
        with Session(engine) as session:
            session.add(booking)
            session.commit()
            session.refresh(booking)
            return booking