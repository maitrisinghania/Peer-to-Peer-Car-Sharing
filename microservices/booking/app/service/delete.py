from sqlalchemy.ext.asyncio import AsyncSession
from app.database.delete_db import delete_booking as db_delete_booking

async def delete_booking(db: AsyncSession, booking_id: int):
    return await db_delete_booking(db, booking_id)