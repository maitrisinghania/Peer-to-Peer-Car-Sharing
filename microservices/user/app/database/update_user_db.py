from sqlalchemy.orm import Session
from ..config.db_config import engine
from ..models.user import User

class UpdateUserDB:
    @staticmethod
    def update_user(user: User) -> User:
        with Session(engine) as session:
            session.add(user)
            session.commit()
            session.refresh(user)
            return user