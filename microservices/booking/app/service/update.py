from sqlalchemy.ext.asyncio import AsyncSession
from app.database.update_db import update_booking as db_update_booking
from app.schemas import BookingUpdate

async def update_booking(db: AsyncSession, booking_id: int, booking_update: BookingUpdate):
    return await db_update_booking(db, booking_id, booking_update)