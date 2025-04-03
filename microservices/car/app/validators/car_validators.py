from typing import List

from ..config.consts import MODEL_NOT_FOUND, ID_NOT_FOUND, INVALID_CAR_DETAILS_TYPE
from ..models.car import Car
from ..exceptions import InvalidBodyException

class CarValidators:
    def sanitize(car: Car) -> None:
        if car.id is not None:
            if type(car.id) != int:
                raise InvalidBodyException(INVALID_CAR_DETAILS_TYPE)
        if car.make is not None:
            if type(car.make) != str:
                raise InvalidBodyException(INVALID_CAR_DETAILS_TYPE)
            else:
                car.make = car.make.strip()
                if car.make == "":
                    car.make = None
        if car.model is not None:
            if type(car.model) != str:
                raise InvalidBodyException(INVALID_CAR_DETAILS_TYPE)
            else:
                car.model = car.model.strip()
                if car.model == "":
                    car.model = None
        if car.year is not None:
            if type(car.year) != int:
                raise InvalidBodyException(INVALID_CAR_DETAILS_TYPE)
        if car.description is not None:
            if type(car.description) != str:
                raise InvalidBodyException(INVALID_CAR_DETAILS_TYPE)
            else:
                car.description = car.description.strip()
                if car.description == "":
                    car.description = None
        if car.price_per_day is not None:
            if type(car.price_per_day) != float:
                raise InvalidBodyException(INVALID_CAR_DETAILS_TYPE)
        if car.available_from is not None:
            if type(car.available_from) != str:
                raise InvalidBodyException(INVALID_CAR_DETAILS_TYPE)
        if car.available_until is not None:
            if type(car.available_until) != str:
                raise InvalidBodyException(INVALID_CAR_DETAILS_TYPE)
        if car.status is not None:
            if type(car.status) != str:
                raise InvalidBodyException(INVALID_CAR_DETAILS_TYPE)
            else:
                car.status = car.status.strip()
                if car.status == "":
                    car.status = None

    def add_validator(car: Car) -> Car:
        CarValidators.sanitize(car)
        if car.make is None or car.model is None:
            raise InvalidBodyException(MODEL_NOT_FOUND)
        car.active = 1
        return car

    def id_validator(car: Car) -> Car:
        CarValidators.sanitize(car)
        if car.id is None:
            raise InvalidBodyException(ID_NOT_FOUND)
        return car

    def list_id_validator(cars: List[Car]) -> List[Car]:
        for car in cars:
            CarValidators.id_validator(car)
        return cars