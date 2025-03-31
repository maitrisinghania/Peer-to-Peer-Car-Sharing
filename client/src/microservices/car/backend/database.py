
import os
from sqlalchemy import create_engine, Column, Integer, String, Float, Date, DateTime, ForeignKey, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime

# Get database URL from environment variable or use default
DATABASE_URL = os.environ.get("DATABASE_URL", "postgresql://postgres:postgres@localhost:5432/sharearider_cars")

# Create SQLAlchemy engine
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Car model
class Car(Base):
    __tablename__ = "cars"

    id = Column(String, primary_key=True)
    owner_id = Column(String, nullable=False)
    make = Column(String, nullable=False)
    model = Column(String, nullable=False)
    year = Column(Integer, nullable=False)
    type = Column(String, nullable=False)
    color = Column(String, nullable=False)
    seats = Column(Integer, nullable=False)
    price_per_day = Column(Float, nullable=False)
    location = Column(String, nullable=False)
    description = Column(String, nullable=True)
    available_from = Column(Date, nullable=True)
    available_to = Column(Date, nullable=True)
    image_url = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.now)

# Create tables
def create_tables():
    Base.metadata.create_all(bind=engine)

# Get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
