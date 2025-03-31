
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

export interface DateRange {
  from: Date | undefined;
  to: Date | undefined;
}
