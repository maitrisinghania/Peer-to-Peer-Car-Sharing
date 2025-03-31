
import { Booking } from "../types";

export const userBookings: Booking[] = [
  {
    id: "booking1",
    carId: "car3",
    renterId: "user_123",
    startDate: "2023-08-10",
    endDate: "2023-08-15",
    status: "confirmed",
    totalPrice: 600,
    createdAt: "2023-08-01T12:00:00Z"
  },
  {
    id: "booking2",
    carId: "car4",
    renterId: "user_123",
    startDate: "2023-09-05",
    endDate: "2023-09-08",
    status: "completed",
    totalPrice: 450,
    createdAt: "2023-08-15T09:30:00Z" 
  }
];

export const receivedBookings: Booking[] = [];  // Bookings received for user's cars
