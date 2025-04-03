from sqlalchemy.ext.asyncio import AsyncSession
from app.database.create_db import create_car as db_create_car
from app.schemas import CarCreate

async def create_car(db: AsyncSession, car: CarCreate):
    return await db_create_car(db, car)