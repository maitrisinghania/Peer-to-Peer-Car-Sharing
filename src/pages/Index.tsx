
import { useState } from "react";
import { useNavigate } from "react-router-dom";
import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";
import { Calendar } from "@/components/ui/calendar";
import { Popover, PopoverContent, PopoverTrigger } from "@/components/ui/popover";
import { Car } from "@/types";
import { CalendarIcon, ChevronRight, MapPin, Search } from "lucide-react";
import { cn } from "@/lib/utils";
import CarCard from "@/components/CarCard";
import BookingModal from "@/components/BookingModal";
import { DateRange } from "react-day-picker";

// Mock data for featured cars
const featuredCars: Car[] = [
  {
    id: "car1",
    ownerId: "user_1",
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
    id: "car2",
    ownerId: "user_2",
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
    id: "car3",
    ownerId: "user_3",
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

const Index = () => {
  const [location, setLocation] = useState("");
  const [dateRange, setDateRange] = useState<DateRange | undefined>({
    from: undefined,
    to: undefined
  });
  const [selectedCar, setSelectedCar] = useState<Car | null>(null);
  const [isBookingModalOpen, setIsBookingModalOpen] = useState(false);
  
  const navigate = useNavigate();
  
  const handleSearchSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    navigate(`/search?location=${location}&from=${dateRange?.from?.toISOString() || ""}&to=${dateRange?.to?.toISOString() || ""}`);
  };
  
  const handleBookClick = (car: Car) => {
    setSelectedCar(car);
    setIsBookingModalOpen(true);
  };
  
  return (
    <div className="flex flex-col min-h-screen">
      {/* Hero Section */}
      <section className="bg-gradient-to-r from-teal-500 to-blue-500 py-16 md:py-24">
        <div className="container mx-auto px-6">
          <div className="max-w-3xl mx-auto text-center text-white mb-12">
            <h1 className="text-4xl md:text-5xl font-bold mb-4">Rent the Perfect Car for Your Journey</h1>
            <p className="text-xl opacity-90">Share your ride or find one nearby. Flexible, convenient, and affordable.</p>
          </div>
          
          <div className="max-w-4xl mx-auto bg-white rounded-lg shadow-lg p-6">
            <form onSubmit={handleSearchSubmit} className="flex flex-col md:flex-row gap-4">
              <div className="flex-1 relative">
                <MapPin className="absolute left-3 top-1/2 transform -translate-y-1/2 text-gray-400" size={18} />
                <Input
                  placeholder="Where do you need a car?"
                  className="pl-10"
                  value={location}
                  onChange={(e) => setLocation(e.target.value)}
                />
              </div>
              
              <Popover>
                <PopoverTrigger asChild>
                  <Button
                    variant="outline"
                    className={cn(
                      "justify-start text-left font-normal w-full md:w-[260px]",
                      !dateRange?.from && "text-muted-foreground"
                    )}
                  >
                    <CalendarIcon className="mr-2 h-4 w-4" />
                    {dateRange?.from ? (
                      dateRange.to ? (
                        <>
                          {dateRange.from.toLocaleDateString()} - {dateRange.to.toLocaleDateString()}
                        </>
                      ) : (
                        dateRange.from.toLocaleDateString()
                      )
                    ) : (
                      <span>Select dates</span>
                    )}
                  </Button>
                </PopoverTrigger>
                <PopoverContent className="w-auto p-0" align="start">
                  <Calendar
                    mode="range"
                    selected={dateRange}
                    onSelect={setDateRange}
                    initialFocus
                  />
                </PopoverContent>
              </Popover>
              
              <Button type="submit" className="md:w-auto">
                <Search className="mr-2 h-4 w-4" /> Search Cars
              </Button>
            </form>
          </div>
        </div>
      </section>
      
      {/* Featured Cars Section */}
      <section className="py-16 px-6 bg-gray-50">
        <div className="container mx-auto">
          <div className="flex justify-between items-center mb-8">
            <h2 className="text-3xl font-bold">Featured Cars</h2>
            <Button variant="outline" onClick={() => navigate("/search")} className="flex items-center">
              View All <ChevronRight size={16} className="ml-1" />
            </Button>
          </div>
          
          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
            {featuredCars.map((car) => (
              <CarCard 
                key={car.id} 
                car={car} 
                onBookClick={handleBookClick}
              />
            ))}
          </div>
        </div>
      </section>
      
      {/* How It Works Section */}
      <section className="py-16 px-6">
        <div className="container mx-auto">
          <h2 className="text-3xl font-bold text-center mb-12">How It Works</h2>
          
          <div className="grid grid-cols-1 md:grid-cols-3 gap-8">
            <div className="bg-white p-6 rounded-lg shadow-sm flex flex-col items-center text-center">
              <div className="bg-teal-100 p-4 rounded-full mb-4">
                <Search size={24} className="text-teal-600" />
              </div>
              <h3 className="text-xl font-semibold mb-2">Find the Perfect Car</h3>
              <p className="text-gray-600">Browse our selection of cars and filter by location, dates, and preferences to find your ideal match.</p>
            </div>
            
            <div className="bg-white p-6 rounded-lg shadow-sm flex flex-col items-center text-center">
              <div className="bg-teal-100 p-4 rounded-full mb-4">
                <CalendarIcon size={24} className="text-teal-600" />
              </div>
              <h3 className="text-xl font-semibold mb-2">Book with Confidence</h3>
              <p className="text-gray-600">Secure your reservation with our easy booking system. Flexible cancellation options available.</p>
            </div>
            
            <div className="bg-white p-6 rounded-lg shadow-sm flex flex-col items-center text-center">
              <div className="bg-teal-100 p-4 rounded-full mb-4">
                <MapPin size={24} className="text-teal-600" />
              </div>
              <h3 className="text-xl font-semibold mb-2">Enjoy Your Journey</h3>
              <p className="text-gray-600">Pick up the car at the arranged location and start your adventure. Return it when you're done.</p>
            </div>
          </div>
        </div>
      </section>
      
      {/* CTA Section */}
      <section className="bg-gray-900 text-white py-16 px-6">
        <div className="container mx-auto max-w-4xl text-center">
          <h2 className="text-3xl md:text-4xl font-bold mb-4">Ready to Share Your Car?</h2>
          <p className="text-xl opacity-80 mb-8">Earn extra income by listing your car when you're not using it.</p>
          <Button size="lg" onClick={() => navigate("/add-car")}>
            List Your Car Now
          </Button>
        </div>
      </section>
      
      <BookingModal 
        car={selectedCar} 
        isOpen={isBookingModalOpen} 
        onClose={() => setIsBookingModalOpen(false)} 
      />
    </div>
  );
};

export default Index;
