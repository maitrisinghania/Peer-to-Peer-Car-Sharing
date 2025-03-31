
import { useState } from "react";
import { useNavigate } from "react-router-dom";
import { Tabs, TabsContent, TabsList, TabsTrigger } from "@/components/ui/tabs";
import { useAuth } from "@/microservices/user/frontend/hooks/use-auth";
import { CarCard } from "@/microservices/car/frontend/components/CarCard";
import { BookingModal } from "@/microservices/booking/frontend/components/BookingModal";
import { Button } from "@/components/ui/button";
import { Car } from "@/microservices/car/frontend/types";
import { Booking } from "@/microservices/booking/frontend/types";
import { userCars, availableCars } from "@/microservices/car/frontend/data/cars";
import { userBookings } from "@/microservices/booking/frontend/data/bookings";
import { formatDate } from "@/lib/utils";
import { Plus } from "lucide-react";

const Dashboard = () => {
  const [selectedCar, setSelectedCar] = useState<Car | null>(null);
  const [isBookingModalOpen, setIsBookingModalOpen] = useState(false);
  const { user } = useAuth();
  const navigate = useNavigate();
  
  const handleBookClick = (car: Car) => {
    setSelectedCar(car);
    setIsBookingModalOpen(true);
  };
  
  return (
    <div className="container mx-auto px-6 py-8">
      <h1 className="text-3xl font-bold mb-6">Welcome, {user?.name}</h1>
      
      <Tabs defaultValue="renter" className="w-full">
        <div className="flex justify-between items-center mb-6">
          <TabsList>
            <TabsTrigger value="renter">Rent a Car</TabsTrigger>
            <TabsTrigger value="owner">My Cars</TabsTrigger>
          </TabsList>
          
          <Button
            variant="outline"
            onClick={() => navigate("/add-car")}
            className="flex items-center gap-2"
          >
            <Plus size={16} />
            Add New Car
          </Button>
        </div>
        
        <TabsContent value="renter" className="space-y-8">
          <section>
            <h2 className="text-2xl font-semibold mb-4">Available Cars</h2>
            {availableCars.length > 0 ? (
              <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
                {availableCars.map((car) => (
                  <CarCard 
                    key={car.id} 
                    car={car} 
                    onBookClick={handleBookClick} 
                  />
                ))}
              </div>
            ) : (
              <div className="bg-gray-50 border rounded-lg p-8 text-center">
                <p className="text-gray-600">No cars available for rent at the moment.</p>
              </div>
            )}
          </section>
          
          <section>
            <h2 className="text-2xl font-semibold mb-4">My Bookings</h2>
            {userBookings.length > 0 ? (
              <div className="bg-white rounded-lg shadow-sm overflow-hidden">
                <table className="min-w-full divide-y divide-gray-200">
                  <thead className="bg-gray-50">
                    <tr>
                      <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Car</th>
                      <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Dates</th>
                      <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Status</th>
                      <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Total</th>
                    </tr>
                  </thead>
                  <tbody className="bg-white divide-y divide-gray-200">
                    {userBookings.map((booking) => {
                      const car = availableCars.find((c) => c.id === booking.carId) || userCars.find((c) => c.id === booking.carId);
                      return (
                        <tr key={booking.id}>
                          <td className="px-6 py-4 whitespace-nowrap">
                            {car ? `${car.make} ${car.model}` : "Unknown Car"}
                          </td>
                          <td className="px-6 py-4 whitespace-nowrap">
                            {formatDate(booking.startDate)} - {formatDate(booking.endDate)}
                          </td>
                          <td className="px-6 py-4 whitespace-nowrap">
                            <span className="px-2 inline-flex text-xs leading-5 font-semibold rounded-full bg-green-100 text-green-800">
                              {booking.status}
                            </span>
                          </td>
                          <td className="px-6 py-4 whitespace-nowrap">
                            ${booking.totalPrice}
                          </td>
                        </tr>
                      );
                    })}
                  </tbody>
                </table>
              </div>
            ) : (
              <div className="bg-gray-50 border rounded-lg p-8 text-center">
                <p className="text-gray-600">You don't have any bookings yet.</p>
                <Button 
                  variant="outline"
                  className="mt-4"
                  onClick={() => document.querySelector('[data-value="renter"]')?.scrollIntoView()}
                >
                  Browse Cars
                </Button>
              </div>
            )}
          </section>
        </TabsContent>
        
        <TabsContent value="owner" className="space-y-6">
          <section>
            <h2 className="text-2xl font-semibold mb-4">My Listed Cars</h2>
            {userCars.length > 0 ? (
              <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
                {userCars.map((car) => (
                  <CarCard 
                    key={car.id} 
                    car={car} 
                    onBookClick={() => navigate(`/car/${car.id}/edit`)} 
                    showBookButton={false}
                  />
                ))}
              </div>
            ) : (
              <div className="bg-gray-50 border rounded-lg p-8 text-center">
                <p className="text-gray-600">You don't have any cars listed yet.</p>
                <Button 
                  className="mt-4"
                  onClick={() => navigate("/add-car")}
                >
                  Add Your First Car
                </Button>
              </div>
            )}
          </section>
          
          <section>
            <h2 className="text-2xl font-semibold mb-4">Booking Requests</h2>
            <div className="bg-gray-50 border rounded-lg p-8 text-center">
              <p className="text-gray-600">No booking requests for your cars at the moment.</p>
            </div>
          </section>
        </TabsContent>
      </Tabs>
      
      <BookingModal 
        car={selectedCar} 
        isOpen={isBookingModalOpen} 
        onClose={() => setIsBookingModalOpen(false)} 
      />
    </div>
  );
};

export default Dashboard;
