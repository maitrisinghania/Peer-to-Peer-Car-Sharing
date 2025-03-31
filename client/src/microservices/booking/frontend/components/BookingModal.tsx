
import { useState } from "react";
import { useNavigate } from "react-router-dom";
import { Car } from "@/microservices/car/frontend/types";
import { useAuth } from "@/microservices/user/frontend/hooks/use-auth";
import { Button } from "@/components/ui/button";
import { Dialog, DialogContent, DialogDescription, DialogFooter, DialogHeader, DialogTitle } from "@/components/ui/dialog";
import { Calendar } from "@/components/ui/calendar";
import { toast } from "sonner";
import { formatCurrency, getDaysCount } from "@/lib/utils";

interface BookingModalProps {
  car: Car | null;
  isOpen: boolean;
  onClose: () => void;
}

export const BookingModal = ({ car, isOpen, onClose }: BookingModalProps) => {
  const [startDate, setStartDate] = useState<Date | undefined>(undefined);
  const [endDate, setEndDate] = useState<Date | undefined>(undefined);
  const [isSubmitting, setIsSubmitting] = useState(false);
  
  const { isAuthenticated, user } = useAuth();
  const navigate = useNavigate();
  
  if (!car) return null;
  
  const handleBooking = async () => {
    if (!isAuthenticated) {
      toast.error("Please sign in to book a car");
      return;
    }
    
    if (!startDate || !endDate) {
      toast.error("Please select start and end dates");
      return;
    }
    
    try {
      setIsSubmitting(true);
      
      // Mock API call - In a real app, this would be an actual API call to booking service
      await new Promise(resolve => setTimeout(resolve, 1000));
      
      const totalDays = getDaysCount(startDate.toISOString(), endDate.toISOString());
      const totalPrice = car.pricePerDay * totalDays;
      
      const bookingData = {
        id: `booking_${Date.now()}`,
        carId: car.id,
        renterId: user?.id,
        startDate: startDate.toISOString(),
        endDate: endDate.toISOString(),
        status: 'confirmed',
        totalPrice: totalPrice,
        createdAt: new Date().toISOString()
      };
      
      // In a real application, we would save this to the booking microservice
      const existingBookings = JSON.parse(localStorage.getItem('bookings') || '[]');
      localStorage.setItem('bookings', JSON.stringify([...existingBookings, bookingData]));
      
      toast.success("Booking confirmed!");
      onClose();
      navigate('/dashboard');
    } catch (error) {
      toast.error("Failed to book the car");
    } finally {
      setIsSubmitting(false);
    }
  };
  
  const handleDateSelect = (date: Date | undefined) => {
    if (!startDate || (startDate && endDate)) {
      setStartDate(date);
      setEndDate(undefined);
    } else {
      if (date && date < startDate) {
        setStartDate(date);
        setEndDate(undefined);
      } else {
        setEndDate(date);
      }
    }
  };
  
  const totalDays = startDate && endDate ? getDaysCount(startDate.toISOString(), endDate.toISOString()) : 0;
  const totalPrice = totalDays * car.pricePerDay;
  
  return (
    <Dialog open={isOpen} onOpenChange={onClose}>
      <DialogContent className="max-w-md">
        <DialogHeader>
          <DialogTitle>Book {car.make} {car.model}</DialogTitle>
          <DialogDescription>
            Select your rental dates to confirm your booking
          </DialogDescription>
        </DialogHeader>
        
        <div className="flex flex-col space-y-4">
          <div className="border rounded-md p-4">
            <h3 className="font-medium mb-2">Select Dates</h3>
            <Calendar
              mode="single"
              selected={undefined}
              onSelect={handleDateSelect}
              disabled={(date) => {
                // Disable dates before today
                return date < new Date(new Date().setHours(0, 0, 0, 0));
              }}
              className="rounded-md border"
            />
            <div className="mt-2 text-sm">
              {startDate && !endDate && (
                <p>Pick your return date</p>
              )}
              {startDate && endDate && (
                <p className="font-medium">
                  {startDate.toLocaleDateString()} - {endDate.toLocaleDateString()}
                  {' '}({totalDays} {totalDays === 1 ? 'day' : 'days'})
                </p>
              )}
            </div>
          </div>
          
          {startDate && endDate && (
            <div className="border rounded-md p-4 space-y-2">
              <h3 className="font-medium">Price Details</h3>
              <div className="flex justify-between text-sm">
                <span>Rate</span>
                <span>{formatCurrency(car.pricePerDay)}/day</span>
              </div>
              <div className="flex justify-between text-sm">
                <span>Duration</span>
                <span>{totalDays} {totalDays === 1 ? 'day' : 'days'}</span>
              </div>
              <div className="flex justify-between font-semibold border-t pt-2 mt-2">
                <span>Total</span>
                <span>{formatCurrency(totalPrice)}</span>
              </div>
            </div>
          )}
        </div>
        
        <DialogFooter>
          <Button variant="outline" onClick={onClose}>Cancel</Button>
          <Button 
            onClick={handleBooking} 
            disabled={!startDate || !endDate || isSubmitting}
          >
            {isSubmitting ? "Processing..." : "Confirm Booking"}
          </Button>
        </DialogFooter>
      </DialogContent>
    </Dialog>
  );
};
