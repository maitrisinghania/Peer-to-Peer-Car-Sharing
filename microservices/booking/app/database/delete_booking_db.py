from sqlalchemy.orm import Session
from ..config.db_config import engine
from ..models.booking import Booking

class DeleteBookingDB:
    @staticmethod
    def delete_booking(booking_id: int) -> Booking:
        with Session(engine) as session:
            booking = session.get(Booking, booking_id)
            if booking:
                session.delete(booking)
                session.commit()
            return booking