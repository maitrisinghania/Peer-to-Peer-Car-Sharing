
import { Car } from "../types";

// Mock data for user's own cars
export const userCars: Car[] = [
  {
    id: "car1",
    ownerId: "user_123",
    make: "Toyota",
    model: "Camry",
    year: 2021,
    type: "Sedan",
    color: "Silver",
    seats: 5,
    pricePerDay: 60,
    imageUrl: "https://images.unsplash.com/photo-1550355291-bbee04a92027?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&h=450&q=80",
    location: "San Francisco, CA",
    availableFrom: "2023-07-01",
    availableTo: "2023-12-31"
  },
  {
    id: "car2",
    ownerId: "user_123",
    make: "Honda",
    model: "CR-V",
    year: 2022,
    type: "SUV",
    color: "Blue",
    seats: 7,
    pricePerDay: 85,
    imageUrl: "https://images.unsplash.com/photo-1568844293986-ca221c6c2801?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&h=450&q=80",
    location: "San Francisco, CA",
    availableFrom: "2023-07-15",
    availableTo: "2023-11-15"
  }
];

// Mock data for available cars (not owned by current user)
export const availableCars: Car[] = [
  {
    id: "car3",
    ownerId: "other_user",
    make: "Tesla",
    model: "Model 3",
    year: 2023,
    type: "Electric",
    color: "Red",
    seats: 5,
    pricePerDay: 120,
    imageUrl: "https://images.unsplash.com/photo-1672702496506-dd7e97f33a5f?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&h=450&q=80",
    location: "Oakland, CA",
    availableFrom: "2023-06-01",
    availableTo: "2023-09-30"
  },
  {
    id: "car4",
    ownerId: "other_user",
    make: "BMW",
    model: "X5",
    year: 2021,
    type: "SUV",
    color: "Black",
    seats: 7,
    pricePerDay: 150,
    imageUrl: "https://images.unsplash.com/photo-1517523267257-396b66993d90?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&h=450&q=80",
    location: "San Jose, CA",
    availableFrom: "2023-07-01",
    availableTo: "2023-10-31"
  }
];

// Featured cars for the homepage
export const featuredCars: Car[] = [
  {
    id: "car5",
    ownerId: "user_2",
    make: "Tesla",
    model: "Model 3",
    year: 2023,
    type: "Electric",
    color: "White",
    seats: 5,
    pricePerDay: 120,
    imageUrl: "https://images.unsplash.com/photo-1672702496506-dd7e97f33a5f?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&h=450&q=80",
    location: "San Francisco, CA",
    availableFrom: "2023-07-01",
    availableTo: "2023-12-31"
  },
  {
    id: "car6",
    ownerId: "user_3",
    make: "Jeep",
    model: "Wrangler",
    year: 2022,
    type: "SUV",
    color: "Red",
    seats: 5,
    pricePerDay: 95,
    imageUrl: "https://images.unsplash.com/photo-1533473359331-0135ef1b58bf?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&h=450&q=80",
    location: "Oakland, CA",
    availableFrom: "2023-07-01",
    availableTo: "2023-12-31"
  },
  {
    id: "car7",
    ownerId: "user_4",
    make: "BMW",
    model: "3 Series",
    year: 2023,
    type: "Sedan",
    color: "Black",
    seats: 5,
    pricePerDay: 110,
    imageUrl: "https://images.unsplash.com/photo-1603584173870-7f23fdae1b7a?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&h=450&q=80",
    location: "San Jose, CA",
    availableFrom: "2023-07-01",
    availableTo: "2023-12-31"
  }
];
