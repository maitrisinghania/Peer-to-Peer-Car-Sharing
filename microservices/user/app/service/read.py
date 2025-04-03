from sqlalchemy.ext.asyncio import AsyncSession
from app.database.read_db import get_user as db_get_user

async def get_user(db: AsyncSession, user_id: int):
    return await db_get_user(db, user_id)