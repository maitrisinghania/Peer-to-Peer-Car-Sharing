from sqlalchemy.ext.asyncio import AsyncSession
from app.database.delete_db import delete_car as db_delete_car

async def delete_car(db: AsyncSession, car_id: int):
    return await db_delete_car(db, car_id)