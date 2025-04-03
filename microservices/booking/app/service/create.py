from sqlalchemy.ext.asyncio import AsyncSession
from app.database.create_db import create_booking as db_create_booking
from app.schemas import BookingCreate

async def create_booking(db: AsyncSession, booking: BookingCreate):
    return await db_create_booking(db, booking)