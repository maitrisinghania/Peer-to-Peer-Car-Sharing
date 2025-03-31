
export interface Booking {
  id: string;
  carId: string;
  renterId: string;
  startDate: string;
  endDate: string;
  status: 'pending' | 'confirmed' | 'cancelled' | 'completed';
  totalPrice: number;
  createdAt: string;
}

export interface ApiResponse<T> {
  data?: T;
  error?: string;
  status: number;
}
