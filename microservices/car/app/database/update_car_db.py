from sqlalchemy.orm import Session
from ..config.db_config import engine
from ..models.car import Car

class UpdateCarDB:
    @staticmethod
    def update_car(car: Car) -> Car:
        with Session(engine) as session:
            session.add(car)
            session.commit()
            session.refresh(car)
            return car