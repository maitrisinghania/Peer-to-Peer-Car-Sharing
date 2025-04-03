from sqlalchemy.ext.asyncio import AsyncSession
from app.database.read_db import get_car as db_get_car

async def get_car(db: AsyncSession, car_id: int):
    return await db_get_car(db, car_id)