from sqlalchemy.ext.asyncio import AsyncSession
from app.database.delete_db import delete_user as db_delete_user

async def delete_user(db: AsyncSession, user_id: int):
    return await db_delete_user(db, user_id)