
export interface Car {
  id: string;
  ownerId: string;
  make: string;
  model: string;
  year: number;
  type: string;
  color: string;
  seats: number;
  pricePerDay: number;
  imageUrl: string;
  location: string;
  description?: string;
  availableFrom?: string;
  availableTo?: string;
}

export interface FilterParams {
  location?: string;
  dateRange?: {
    from: Date | undefined;
    to: Date | undefined;
  };
  priceRange?: {
    min: number;
    max: number;
  };
  carType?: string[];
  make?: string[];
  seats?: number;
}

export interface User {
  id: string;
  email: string;
  name: string;
  phone?: string;
  isAuthenticated: boolean;
}

export interface Booking {
  id: string;
  carId: string;
  renterId: string;
  startDate: string;
  endDate: string;
  status: string;
  totalPrice: number;
  createdAt: string;
}
