
import { Car } from "@/types";
import { Card, CardContent, CardFooter, CardHeader } from "@/components/ui/card";
import { Button } from "@/components/ui/button";
import { Badge } from "@/components/ui/badge";
import { Calendar, MapPin, User } from "lucide-react";
import { formatCurrency } from "@/lib/utils";

interface CarCardProps {
  car: Car;
  onBookClick?: (car: Car) => void;
  showBookButton?: boolean;
}

const CarCard = ({ car, onBookClick, showBookButton = true }: CarCardProps) => {
  return (
    <Card className="h-full overflow-hidden transition-all hover:shadow-md">
      <div className="relative aspect-[16/9] w-full overflow-hidden">
        <img 
          src={car.imageUrl} 
          alt={`${car.make} ${car.model}`}
          className="h-full w-full object-cover transition-transform duration-300 hover:scale-105"
        />
        <Badge 
          className="absolute top-2 right-2 bg-teal-500 text-white"
        >
          {formatCurrency(car.pricePerDay)}/day
        </Badge>
      </div>
      
      <CardHeader className="pb-2">
        <div className="flex justify-between items-start">
          <div>
            <h3 className="font-bold text-lg">{car.make} {car.model}</h3>
            <p className="text-gray-500 text-sm">{car.year}</p>
          </div>
          <Badge variant="outline" className="text-orange-600 border-orange-600">
            {car.type}
          </Badge>
        </div>
      </CardHeader>
      
      <CardContent className="pb-4">
        <div className="flex flex-col gap-2 text-sm">
          <div className="flex items-center gap-2">
            <MapPin size={14} className="text-gray-400" />
            <span>{car.location}</span>
          </div>
          <div className="flex items-center gap-2">
            <User size={14} className="text-gray-400" />
            <span>{car.seats} seats</span>
          </div>
          {car.availableFrom && car.availableTo && (
            <div className="flex items-center gap-2">
              <Calendar size={14} className="text-gray-400" />
              <span>Available: {new Date(car.availableFrom).toLocaleDateString()} - {new Date(car.availableTo).toLocaleDateString()}</span>
            </div>
          )}
        </div>
      </CardContent>
      
      {showBookButton && (
        <CardFooter>
          <Button 
            className="w-full"
            onClick={() => onBookClick && onBookClick(car)}
          >
            Book Now
          </Button>
        </CardFooter>
      )}
    </Card>
  );
};

export default CarCard;
