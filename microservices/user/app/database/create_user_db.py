from sqlalchemy.orm import Session
from ..config.db_config import engine
from ..models.user import User

class CreateUserDB:
    @staticmethod
    def add_user(user: User) -> User:
        with Session(engine) as session:
            session.add(user)
            session.commit()
            session.refresh(user)
            return user