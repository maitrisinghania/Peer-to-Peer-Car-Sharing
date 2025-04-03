from sqlalchemy.ext.asyncio import AsyncSession
from app.database.update_db import update_car as db_update_car
from app.schemas import CarUpdate

async def update_car(db: AsyncSession, car_id: int, car_update: CarUpdate):
    return await db_update_car(db, car_id, car_update)