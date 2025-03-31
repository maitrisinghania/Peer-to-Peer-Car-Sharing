
from fastapi import FastAPI, HTTPException, Query, status, Depends
from fastapi.middleware.cors import CORSMiddleware
from typing import List, Optional
from sqlalchemy.orm import Session
import uuid
from datetime import date, datetime
import uvicorn
from .database import get_db, create_tables, Car as CarModel
from .models import CarBase, CarCreate, CarUpdate, CarResponse

app = FastAPI(title="Car Service", description="Car management for ShareARider platform")

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

# Create tables on startup
@app.on_event("startup")
def startup_event():
    create_tables()

# Routes
@app.get("/")
async def root():
    return {"message": "Car Service API"}

@app.get("/cars/", response_model=List[CarResponse])
async def get_cars(
    location: Optional[str] = None,
    available_from: Optional[date] = None,
    available_to: Optional[date] = None,
    make: Optional[str] = None,
    model: Optional[str] = None,
    car_type: Optional[str] = None,
    min_price: Optional[float] = None,
    max_price: Optional[float] = None,
    skip: int = Query(0, ge=0),
    limit: int = Query(100, ge=1, le=100),
    db: Session = Depends(get_db)
):
    query = db.query(CarModel)
    
    # Apply filters
    if location:
        query = query.filter(CarModel.location.ilike(f"%{location}%"))
    
    if available_from and available_to:
        query = query.filter(CarModel.available_from <= available_from)
        query = query.filter(CarModel.available_to >= available_to)
    
    if make:
        query = query.filter(CarModel.make.ilike(f"%{make}%"))
    
    if model:
        query = query.filter(CarModel.model.ilike(f"%{model}%"))
    
    if car_type:
        query = query.filter(CarModel.type.ilike(f"%{car_type}%"))
    
    if min_price is not None:
        query = query.filter(CarModel.price_per_day >= min_price)
    
    if max_price is not None:
        query = query.filter(CarModel.price_per_day <= max_price)
    
    # Apply pagination
    query = query.offset(skip).limit(limit)
    
    return query.all()

@app.get("/cars/{car_id}", response_model=CarResponse)
async def get_car(car_id: str, db: Session = Depends(get_db)):
    car = db.query(CarModel).filter(CarModel.id == car_id).first()
    if not car:
        raise HTTPException(status_code=404, detail="Car not found")
    return car

@app.get("/cars/owner/{owner_id}", response_model=List[CarResponse])
async def get_owner_cars(owner_id: str, db: Session = Depends(get_db)):
    return db.query(CarModel).filter(CarModel.owner_id == owner_id).all()

@app.post("/cars/", response_model=CarResponse, status_code=status.HTTP_201_CREATED)
async def create_car(car: CarCreate, owner_id: str, db: Session = Depends(get_db)):
    car_id = f"car_{uuid.uuid4()}"
    
    db_car = CarModel(
        id=car_id,
        owner_id=owner_id,
        **car.dict()
    )
    
    db.add(db_car)
    db.commit()
    db.refresh(db_car)
    return db_car

@app.put("/cars/{car_id}", response_model=CarResponse)
async def update_car(car_id: str, car: CarUpdate, owner_id: str, db: Session = Depends(get_db)):
    db_car = db.query(CarModel).filter(CarModel.id == car_id).first()
    if not db_car:
        raise HTTPException(status_code=404, detail="Car not found")
    
    if db_car.owner_id != owner_id:
        raise HTTPException(status_code=403, detail="Not authorized to update this car")
    
    # Update fields if provided
    update_data = car.dict(exclude_unset=True)
    for key, value in update_data.items():
        setattr(db_car, key, value)
    
    db.commit()
    db.refresh(db_car)
    return db_car

@app.delete("/cars/{car_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_car(car_id: str, owner_id: str, db: Session = Depends(get_db)):
    db_car = db.query(CarModel).filter(CarModel.id == car_id).first()
    if not db_car:
        raise HTTPException(status_code=404, detail="Car not found")
    
    if db_car.owner_id != owner_id:
        raise HTTPException(status_code=403, detail="Not authorized to delete this car")
    
    db.delete(db_car)
    db.commit()
    return None

if __name__ == "__main__":
    uvicorn.run("server:app", host="0.0.0.0", port=8002, reload=True)
