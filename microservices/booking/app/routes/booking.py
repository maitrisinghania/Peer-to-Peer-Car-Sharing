from fastapi import APIRouter, Query
from fastapi import Depends, Security

from typing import Dict, List, Optional

from ..config import logger
from ..config.consts import PATH_PREFIX_BOOKING, BookingRoutes, ORG

from ..models.booking import Booking, ExceptionClass

from ..service import CreateBookingService, ReadBookingService, UpdateBookingService, DeleteBookingService

from ..utils import VerifyToken, BookingValidators, set_org_model, set_org_multiple_model

apiRouter = APIRouter(prefix=PATH_PREFIX_BOOKING)
auth = VerifyToken()

bad_request_responses = {
    400: {
        "description": "Error: Bad Request",
        "model": ExceptionClass
    }
}

auth_responses = {
    401: {
        "description": "Error: Unauthorized",
        "model": ExceptionClass
    },
    403: {
        "description": "Error: Forbidden",
        "model": ExceptionClass
    }
}

@apiRouter.post(BookingRoutes.POST_ADD_BOOKING, response_model=Booking, responses=bad_request_responses | auth_responses)
async def add_booking(booking: Booking = Depends(BookingValidators.add_validator), auth_result: Dict = Security(auth.verify)) -> Booking:
    set_org_model(booking, auth_result)
    logger.debug("In add_booking:" + str(booking))
    return CreateBookingService.add_booking(booking)

@apiRouter.put(BookingRoutes.PUT_DEACTIVATE_BOOKINGS, response_model=List[Booking], responses=auth_responses)
async def deactivate_bookings(bookings: List[Booking] = Depends(BookingValidators.list_id_validator), auth_result: Dict = Security(auth.verify)) -> List[Booking]:
    set_org_multiple_model(bookings, auth_result)
    logger.debug("In deactivate_bookings:" + str(bookings))
    UpdateBookingService.deactivate_bookings(bookings)
    return await get_all_bookings(auth_result)

@apiRouter.put(BookingRoutes.PUT_RECOVER_BOOKINGS, response_model=List[Booking], responses=auth_responses)
async def recover_bookings(bookings: List[Booking] = Depends(BookingValidators.list_id_validator), auth_result: Dict = Security(auth.verify)) -> List[Booking]:
    set_org_multiple_model(bookings, auth_result)
    logger.debug("In recover_bookings:" + str(bookings))
    UpdateBookingService.recover_bookings(bookings)
    return await get_deleted_bookings(auth_result)

@apiRouter.put(BookingRoutes.PUT_BOOKING_ADDED_IN_TRANS, response_model=Booking, responses=bad_request_responses | auth_responses)
async def booking_added_in_trans(booking: Booking = Depends(BookingValidators.id_validator), auth_result: Dict = Security(auth.verify)) -> Booking:
    set_org_model(booking, auth_result)
    logger.debug("In booking_added_in_trans:" + str(booking))
    return UpdateBookingService.booking_in_transaction(booking)

@apiRouter.put(BookingRoutes.PUT_BOOKING_ROLLBACK_IN_TRANS, response_model=Booking, responses=bad_request_responses | auth_responses)
async def rollback_added_in_trans(booking: Booking = Depends(BookingValidators.rollback_validator), auth_result: Dict = Security(auth.verify)) -> Booking:
    set_org_model(booking, auth_result)
    logger.debug("In rollback_added_in_trans:" + str(booking))
    return UpdateBookingService.booking_rollback_in_trans(booking)

@apiRouter.get(BookingRoutes.GET_BOOKING + "/{booking_id}", response_model=Booking, responses=bad_request_responses | auth_responses)
async def get_booking(booking_id: int, auth_result: Dict = Security(auth.verify)) -> Booking:
    booking : Booking = Booking(id = booking_id)
    set_org_model(booking, auth_result)
    logger.debug("In get_booking:" + str(booking))
    return ReadBookingService.get_booking(booking)

@apiRouter.get(BookingRoutes.GET_ALL_BOOKINGS, response_model=List[Booking], responses=auth_responses)
async def get_all_bookings(auth_result: Dict = Security(auth.verify)) -> List[Booking]:
    booking : Booking = set_org_model(Booking(), auth_result)
    logger.debug("In get_all_bookings:" + str(booking))
    return ReadBookingService.get_all_bookings(booking)

@apiRouter.get(BookingRoutes.GET_BOOKINGS_LIST+"/", response_model=List[Optional[Booking]], responses=auth_responses)
async def get_bookings_list(booking_id: List[int] = Query([]), auth_result: Dict = Security(auth.verify)) -> List[Optional[Booking]]:
    logger.debug("In get_bookings_list:" + str(booking_id))
    return ReadBookingService.get_bookings_list(auth_result[ORG], booking_id)

@apiRouter.get(BookingRoutes.GET_DELETED_BOOKINGS, response_model=List[Booking], responses=auth_responses)
async def get_deleted_bookings(auth_result: Dict = Security(auth.verify)) -> List[Booking]:
    booking : Booking = set_org_model(Booking(), auth_result)
    logger.debug("In get_deleted_bookings:" + str(booking))
    return ReadBookingService.get_deleted_bookings(booking)

@apiRouter.delete(BookingRoutes.DELETE_BOOKINGS, response_model=List[Booking], responses=auth_responses)
async def delete_bookings(bookings: List[Booking] = Depends(BookingValidators.list_id_validator), auth_result: Dict = Security(auth.verify)) -> List[Booking]:
    set_org_multiple_model(bookings, auth_result)
    logger.debug("In delete_bookings:" + str(bookings))
    DeleteBookingService.delete_bookings(bookings)
    return await get_deleted_bookings(auth_result)