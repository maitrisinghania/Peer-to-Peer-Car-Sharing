
import { useState } from "react";
import { FilterParams } from "../types";
import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";
import { Label } from "@/components/ui/label";
import { Calendar } from "@/components/ui/calendar";
import { Popover, PopoverContent, PopoverTrigger } from "@/components/ui/popover";
import { Checkbox } from "@/components/ui/checkbox";
import { Slider } from "@/components/ui/slider";
import { CalendarIcon, Search } from "lucide-react";
import { formatDate } from "@/lib/utils";
import { cn } from "@/lib/utils";

interface CarFiltersProps {
  onFilterChange: (filters: FilterParams) => void;
}

const carTypes = ["Sedan", "SUV", "Truck", "Convertible", "Sports", "Electric", "Hybrid"];
const carMakes = ["Toyota", "Honda", "Ford", "BMW", "Mercedes", "Tesla", "Audi"];

export const CarFilters = ({ onFilterChange }: CarFiltersProps) => {
  const [filters, setFilters] = useState<FilterParams>({
    location: "",
    dateRange: { from: undefined, to: undefined },
    priceRange: { min: 0, max: 500 },
    carType: [],
    make: [],
    seats: 0
  });
  
  const handleInputChange = (key: keyof FilterParams, value: any) => {
    const updatedFilters = { ...filters, [key]: value };
    setFilters(updatedFilters);
  };
  
  const handleCheckboxChange = (category: 'carType' | 'make', value: string) => {
    const currentValues = filters[category] as string[] || [];
    let newValues: string[];
    
    if (currentValues.includes(value)) {
      newValues = currentValues.filter(item => item !== value);
    } else {
      newValues = [...currentValues, value];
    }
    
    handleInputChange(category, newValues);
  };
  
  const handleApplyFilters = () => {
    onFilterChange(filters);
  };
  
  return (
    <div className="bg-white p-6 rounded-lg shadow-md">
      <h2 className="font-semibold text-lg mb-4">Find Your Perfect Ride</h2>
      
      {/* Location filter */}
      <div className="mb-4">
        <Label htmlFor="location">Location</Label>
        <div className="relative">
          <Search className="absolute left-3 top-2.5 h-4 w-4 text-muted-foreground" />
          <Input
            id="location"
            placeholder="Enter city or address"
            className="pl-10"
            value={filters.location}
            onChange={(e) => handleInputChange("location", e.target.value)}
          />
        </div>
      </div>
      
      {/* Date range filter */}
      <div className="mb-4">
        <Label>Date Range</Label>
        <Popover>
          <PopoverTrigger asChild>
            <Button
              variant="outline"
              className="w-full justify-start text-left font-normal"
            >
              <CalendarIcon className="mr-2 h-4 w-4" />
              {filters.dateRange?.from ? (
                filters.dateRange.to ? (
                  <>
                    {formatDate(filters.dateRange.from.toISOString())} - {formatDate(filters.dateRange.to.toISOString())}
                  </>
                ) : (
                  formatDate(filters.dateRange.from.toISOString())
                )
              ) : (
                <span>Pick a date range</span>
              )}
            </Button>
          </PopoverTrigger>
          <PopoverContent className="w-auto p-0" align="start">
            <Calendar
              mode="range"
              selected={{
                from: filters.dateRange?.from,
                to: filters.dateRange?.to,
              }}
              onSelect={(range) => handleInputChange("dateRange", range)}
              initialFocus
            />
          </PopoverContent>
        </Popover>
      </div>
      
      {/* Price range filter */}
      <div className="mb-6">
        <Label>Price Range (per day)</Label>
        <div className="pt-4 px-2">
          <Slider
            defaultValue={[filters.priceRange?.min || 0, filters.priceRange?.max || 500]}
            max={500}
            step={10}
            onValueChange={(values) => 
              handleInputChange("priceRange", { min: values[0], max: values[1] })
            }
          />
          <div className="flex justify-between mt-2 text-sm">
            <span>${filters.priceRange?.min}</span>
            <span>${filters.priceRange?.max}</span>
          </div>
        </div>
      </div>
      
      {/* Car type filter */}
      <div className="mb-4">
        <Label className="block mb-2">Car Type</Label>
        <div className="grid grid-cols-2 gap-2">
          {carTypes.map((type) => (
            <div key={type} className="flex items-center space-x-2">
              <Checkbox
                id={`type-${type}`}
                checked={(filters.carType || []).includes(type)}
                onCheckedChange={() => handleCheckboxChange("carType", type)}
              />
              <label
                htmlFor={`type-${type}`}
                className="text-sm font-medium leading-none peer-disabled:cursor-not-allowed peer-disabled:opacity-70"
              >
                {type}
              </label>
            </div>
          ))}
        </div>
      </div>
      
      {/* Car make filter */}
      <div className="mb-6">
        <Label className="block mb-2">Car Make</Label>
        <div className="grid grid-cols-2 gap-2">
          {carMakes.map((make) => (
            <div key={make} className="flex items-center space-x-2">
              <Checkbox
                id={`make-${make}`}
                checked={(filters.make || []).includes(make)}
                onCheckedChange={() => handleCheckboxChange("make", make)}
              />
              <label
                htmlFor={`make-${make}`}
                className="text-sm font-medium leading-none peer-disabled:cursor-not-allowed peer-disabled:opacity-70"
              >
                {make}
              </label>
            </div>
          ))}
        </div>
      </div>
      
      <Button className="w-full" onClick={handleApplyFilters}>
        Apply Filters
      </Button>
    </div>
  );
};
