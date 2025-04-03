from sqlalchemy.orm import Session
from ..config.db_config import engine
from ..models.car import Car

class ReadCarDB:
    @staticmethod
    def get_car(car_id: int) -> Car:
        with Session(engine) as session:
            car = session.get(Car, car_id)
            return car