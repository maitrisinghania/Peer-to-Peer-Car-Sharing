from typing import List

from ..config.consts import MODEL_NOT_FOUND, ID_NOT_FOUND, INVALID_BOOKING_DETAILS_TYPE
from ..models.booking import Booking
from ..exceptions import InvalidBodyException

class BookingValidators:
    def sanitize(booking: Booking) -> None:
        if booking.id is not None:
            if type(booking.id) != int:
                raise InvalidBodyException(INVALID_BOOKING_DETAILS_TYPE)
        if booking.user_id is not None:
            if type(booking.user_id) != int:
                raise InvalidBodyException(INVALID_BOOKING_DETAILS_TYPE)
        if booking.car_id is not None:
            if type(booking.car_id) != int:
                raise InvalidBodyException(INVALID_BOOKING_DETAILS_TYPE)
        if booking.start_date is not None:
            if type(booking.start_date) != str:
                raise InvalidBodyException(INVALID_BOOKING_DETAILS_TYPE)
        if booking.end_date is not None:
            if type(booking.end_date) != str:
                raise InvalidBodyException(INVALID_BOOKING_DETAILS_TYPE)
        if booking.status is not None:
            if type(booking.status) != str:
                raise InvalidBodyException(INVALID_BOOKING_DETAILS_TYPE)
            else:
                booking.status = booking.status.strip()
                if booking.status == "":
                    booking.status = None

    def add_validator(booking: Booking) -> Booking:
        BookingValidators.sanitize(booking)
        if booking.user_id is None or booking.car_id is None:
            raise InvalidBodyException(MODEL_NOT_FOUND)
        booking.active = 1
        return booking

    def id_validator(booking: Booking) -> Booking:
        BookingValidators.sanitize(booking)
        if booking.id is None:
            raise InvalidBodyException(ID_NOT_FOUND)
        return booking

    def list_id_validator(bookings: List[Booking]) -> List[Booking]:
        for booking in bookings:
            BookingValidators.id_validator(booking)
        return bookings