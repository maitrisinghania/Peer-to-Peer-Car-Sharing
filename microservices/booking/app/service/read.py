from sqlalchemy.ext.asyncio import AsyncSession
from app.database.read_db import get_booking as db_get_booking

async def get_booking(db: AsyncSession, booking_id: int):
    return await db_get_booking(db, booking_id)