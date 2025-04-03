from sqlalchemy.ext.asyncio import AsyncSession
from app.database.create_db import create_user as db_create_user
from app.schemas import UserCreate

async def create_user(db: AsyncSession, user: UserCreate):
    return await db_create_user(db, user)