
from fastapi import FastAPI, HTTPException, Depends, Query, status
from fastapi.middleware.cors import CORSMiddleware
from typing import List, Optional
from sqlalchemy.orm import Session
import uuid
from datetime import date, datetime
import uvicorn
from .database import get_db, create_tables, Booking as BookingModel
from .models import BookingBase, BookingCreate, BookingUpdate, BookingResponse

app = FastAPI(title="Booking Service", description="Booking management for ShareARider platform")

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
    return {"message": "Booking Service API"}

@app.get("/bookings/", response_model=List[BookingResponse])
async def get_bookings(
    car_id: Optional[str] = None,
    renter_id: Optional[str] = None,
    status: Optional[str] = None,
    skip: int = Query(0, ge=0),
    limit: int = Query(100, ge=1, le=100),
    db: Session = Depends(get_db)
):
    query = db.query(BookingModel)
    
    # Apply filters
    if car_id:
        query = query.filter(BookingModel.car_id == car_id)
    
    if renter_id:
        query = query.filter(BookingModel.renter_id == renter_id)
    
    if status:
        query = query.filter(BookingModel.status == status)
    
    # Apply pagination
    query = query.offset(skip).limit(limit)
    
    return query.all()

@app.get("/bookings/{booking_id}", response_model=BookingResponse)
async def get_booking(booking_id: str, db: Session = Depends(get_db)):
    booking = db.query(BookingModel).filter(BookingModel.id == booking_id).first()
    if not booking:
        raise HTTPException(status_code=404, detail="Booking not found")
    return booking

@app.post("/bookings/", response_model=BookingResponse, status_code=status.HTTP_201_CREATED)
async def create_booking(booking: BookingCreate, db: Session = Depends(get_db)):
    # Check if car is available for the requested dates
    # This would involve calling the Car Service in a real microservices architecture
    
    booking_id = f"booking_{uuid.uuid4()}"
    
    db_booking = BookingModel(
        id=booking_id,
        status="pending",
        **booking.dict()
    )
    
    db.add(db_booking)
    db.commit()
    db.refresh(db_booking)
    return db_booking

@app.put("/bookings/{booking_id}", response_model=BookingResponse)
async def update_booking(booking_id: str, booking: BookingUpdate, user_id: str, db: Session = Depends(get_db)):
    db_booking = db.query(BookingModel).filter(BookingModel.id == booking_id).first()
    if not db_booking:
        raise HTTPException(status_code=404, detail="Booking not found")
    
    # Check authorization
    if db_booking.renter_id != user_id:
        # In a real app, we would also check if the user is the car owner
        raise HTTPException(status_code=403, detail="Not authorized to update this booking")
    
    # Update fields if provided
    update_data = booking.dict(exclude_unset=True)
    for key, value in update_data.items():
        setattr(db_booking, key, value)
    
    db.commit()
    db.refresh(db_booking)
    return db_booking

@app.delete("/bookings/{booking_id}", status_code=status.HTTP_204_NO_CONTENT)
async def cancel_booking(booking_id: str, user_id: str, db: Session = Depends(get_db)):
    db_booking = db.query(BookingModel).filter(BookingModel.id == booking_id).first()
    if not db_booking:
        raise HTTPException(status_code=404, detail="Booking not found")
    
    # Check authorization
    if db_booking.renter_id != user_id:
        # In a real app, we would also check if the user is the car owner
        raise HTTPException(status_code=403, detail="Not authorized to cancel this booking")
    
    # In a real app, we might not delete but set status to canceled
    db_booking.status = "cancelled"
    db.commit()
    return None

if __name__ == "__main__":
    uvicorn.run("server:app", host="0.0.0.0", port=8003, reload=True)
