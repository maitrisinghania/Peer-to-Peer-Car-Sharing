from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from .config import get_db_settings

settings = get_db_settings()

engine = create_async_engine(settings.DATABASE_URL, echo=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine, class_=AsyncSession)
Base = declarative_base()

def create_db_and_tables():
    from app.models import Car
    Base.metadata.create_all(bind=engine)

async def get_db():
    async with SessionLocal() as session:
        yield session