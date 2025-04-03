from fastapi import APIRouter, Query
from fastapi import Depends, Security

from typing import Dict, List, Optional

from ..config import logger
from ..config.consts import PATH_PREFIX_CAR, CarRoutes, ORG

from ..models.car import Car, ExceptionClass

from ..service import CreateCarService, ReadCarService, UpdateCarService, DeleteCarService

from ..utils import VerifyToken, CarValidators, set_org_model, set_org_multiple_model

apiRouter = APIRouter(prefix=PATH_PREFIX_CAR)
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

@apiRouter.post(CarRoutes.POST_ADD_CAR, response_model=Car, responses=bad_request_responses | auth_responses)
async def add_car(car: Car = Depends(CarValidators.add_validator), auth_result: Dict = Security(auth.verify)) -> Car:
    set_org_model(car, auth_result)
    logger.debug("In add_car:" + str(car))
    return CreateCarService.add_car(car)

@apiRouter.put(CarRoutes.PUT_DEACTIVATE_CARS, response_model=List[Car], responses=auth_responses)
async def deactivate_cars(cars: List[Car] = Depends(CarValidators.list_id_validator), auth_result: Dict = Security(auth.verify)) -> List[Car]:
    set_org_multiple_model(cars, auth_result)
    logger.debug("In deactivate_cars:" + str(cars))
    UpdateCarService.deactivate_cars(cars)
    return await get_all_cars(auth_result)

@apiRouter.put(CarRoutes.PUT_RECOVER_CARS, response_model=List[Car], responses=auth_responses)
async def recover_cars(cars: List[Car] = Depends(CarValidators.list_id_validator), auth_result: Dict = Security(auth.verify)) -> List[Car]:
    set_org_multiple_model(cars, auth_result)
    logger.debug("In recover_cars:" + str(cars))
    UpdateCarService.recover_cars(cars)
    return await get_deleted_cars(auth_result)

@apiRouter.put(CarRoutes.PUT_CAR_ADDED_IN_TRANS, response_model=Car, responses=bad_request_responses | auth_responses)
async def car_added_in_trans(car: Car = Depends(CarValidators.id_validator), auth_result: Dict = Security(auth.verify)) -> Car:
    set_org_model(car, auth_result)
    logger.debug("In car_added_in_trans:" + str(car))
    return UpdateCarService.car_in_transaction(car)

@apiRouter.put(CarRoutes.PUT_CAR_ROLLBACK_IN_TRANS, response_model=Car, responses=bad_request_responses | auth_responses)
async def rollback_added_in_trans(car: Car = Depends(CarValidators.rollback_validator), auth_result: Dict = Security(auth.verify)) -> Car:
    set_org_model(car, auth_result)
    logger.debug("In rollback_added_in_trans:" + str(car))
    return UpdateCarService.car_rollback_in_trans(car)

@apiRouter.get(CarRoutes.GET_CAR + "/{car_id}", response_model=Car, responses=bad_request_responses | auth_responses)
async def get_car(car_id: int, auth_result: Dict = Security(auth.verify)) -> Car:
    car : Car = Car(id = car_id)
    set_org_model(car, auth_result)
    logger.debug("In get_car:" + str(car))
    return ReadCarService.get_car(car)

@apiRouter.get(CarRoutes.GET_ALL_CARS, response_model=List[Car], responses=auth_responses)
async def get_all_cars(auth_result: Dict = Security(auth.verify)) -> List[Car]:
    car : Car = set_org_model(Car(), auth_result)
    logger.debug("In get_all_cars:" + str(car))
    return ReadCarService.get_all_cars(car)

@apiRouter.get(CarRoutes.GET_CARS_LIST+"/", response_model=List[Optional[Car]], responses=auth_responses)
async def get_cars_list(car_id: List[int] = Query([]), auth_result: Dict = Security(auth.verify)) -> List[Optional[Car]]:
    logger.debug("In get_cars_list:" + str(car_id))
    return ReadCarService.get_cars_list(auth_result[ORG], car_id)

@apiRouter.get(CarRoutes.GET_DELETED_CARS, response_model=List[Car], responses=auth_responses)
async def get_deleted_cars(auth_result: Dict = Security(auth.verify)) -> List[Car]:
    car : Car = set_org_model(Car(), auth_result)
    logger.debug("In get_deleted_cars:" + str(car))
    return ReadCarService.get_deleted_cars(car)

@apiRouter.delete(CarRoutes.DELETE_CARS, response_model=List[Car], responses=auth_responses)
async def delete_cars(cars: List[Car] = Depends(CarValidators.list_id_validator), auth_result: Dict = Security(auth.verify)) -> List[Car]:
    set_org_multiple_model(cars, auth_result)
    logger.debug("In delete_cars:" + str(cars))
    DeleteCarService.delete_cars(cars)
    return await get_deleted_cars(auth_result)