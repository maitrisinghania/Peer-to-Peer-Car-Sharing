
import { Car } from "../types";
import { formatCurrency } from "../lib/utils";

interface CarCardProps {
  car: Car;
  onBookClick?: (car: Car) => void;
  showBookButton?: boolean;
}

export const CarCard = ({ car, onBookClick, showBookButton = true }: CarCardProps) => {
  return (
    <div className="border rounded-lg overflow-hidden shadow-sm hover:shadow-md transition-all h-full">
      <div className="relative aspect-[16/9] w-full overflow-hidden">
        <img 
          src={car.imageUrl} 
          alt={`${car.make} ${car.model}`}
          className="h-full w-full object-cover transition-transform duration-300 hover:scale-105"
        />
        <div className="absolute top-2 right-2 bg-teal-500 text-white text-sm px-2 py-1 rounded-full">
          {formatCurrency(car.pricePerDay)}/day
        </div>
      </div>
      
      <div className="p-4">
        <div className="flex justify-between items-start">
          <div>
            <h3 className="font-bold text-lg">{car.make} {car.model}</h3>
            <p className="text-gray-500 text-sm">{car.year}</p>
          </div>
          <div className="text-orange-600 border border-orange-600 text-xs px-2 py-1 rounded-full">
            {car.type}
          </div>
        </div>
        
        <div className="mt-4 space-y-2 text-sm">
          <div className="flex items-center gap-2">
            <span className="text-gray-400">📍</span>
            <span>{car.location}</span>
          </div>
          <div className="flex items-center gap-2">
            <span className="text-gray-400">👤</span>
            <span>{car.seats} seats</span>
          </div>
          {car.availableFrom && car.availableTo && (
            <div className="flex items-center gap-2">
              <span className="text-gray-400">📅</span>
              <span>Available: {new Date(car.availableFrom).toLocaleDateString()} - {new Date(car.availableTo).toLocaleDateString()}</span>
            </div>
          )}
        </div>
      </div>
      
      {showBookButton && (
        <div className="px-4 pb-4">
          <button 
            className="w-full bg-blue-600 text-white py-2 px-4 rounded hover:bg-blue-700 transition-colors"
            onClick={() => onBookClick && onBookClick(car)}
          >
            Book Now
          </button>
        </div>
      )}
    </div>
  );
};

export default CarCard;
