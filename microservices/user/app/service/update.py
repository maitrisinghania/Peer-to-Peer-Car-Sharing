from sqlalchemy.ext.asyncio import AsyncSession
from app.database.update_db import update_user as db_update_user
from app.schemas import UserUpdate

async def update_user(db: AsyncSession, user_id: int, user_update: UserUpdate):
    return await db_update_user(db, user_id, user_update)