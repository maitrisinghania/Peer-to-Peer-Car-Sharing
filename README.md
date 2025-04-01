
# Peer to Peer - Car Sharing Platform

## Overview
This project is a peer-to-peer car sharing platform that allows car owners to rent out their vehicles when they're not using them, and renters to find convenient, affordable transportation.

## Microservices Architecture
The project follows a microservices architecture with three main services:

1. **User Service**
   - Manages user authentication and profiles
   - Stores user preferences and settings

2. **Car Service**
   - Manages car listings and details
   - Handles car search and filtering
   - Manages car availability

3. **Booking Service**
   - Handles booking creation and management
   - Manages booking status (confirmed, canceled, completed)

## Project Structure
```
frontend/                # React frontend application
├── src/
│   ├── components/      # Shared UI components
│   ├── layouts/         # Layout components
│   ├── lib/             # Shared utility functions
│   ├── pages/           # Main pages
│   └── types/           # TypeScript type definitions
│
microservices/
├── user/
│   └── backend/         # User service backend (FastAPI)
│    
├── car/
│   └── backend/         # Car service backend (FastAPI)
│   
└── booking/
    └── backend/         # Booking service backend (FastAPI)
```


## Features
- User registration and authentication
- Car listing and management
- Search and filter cars by location, date, price
- Booking management
- Dashboard views for both car owners and renters
