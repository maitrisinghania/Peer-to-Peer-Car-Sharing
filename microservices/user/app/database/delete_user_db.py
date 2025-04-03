from sqlalchemy.orm import Session
from ..config.db_config import engine
from ..models.user import User

class DeleteUserDB:
    @staticmethod
    def delete_user(user_id: int) -> User:
        with Session(engine) as session:
            user = session.get(User, user_id)
            if user:
                session.delete(user)
                session.commit()
            return user