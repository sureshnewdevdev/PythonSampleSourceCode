class Car:
    """A simple attempt to represent a car."""
    
    # Class variable (shared by all instances)
    vehicle_type = "automobile"
    
    def __init__(self, make, model, year):
        # Instance variables (unique to each instance)
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0  # Default value
    
    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        return f"{self.year} {self.make} {self.model}"
    
    def read_odometer(self):
        """Print the car's mileage."""
        print(f"This car has {self.odometer_reading} miles on it.")

car1 = Car('Toyota', 'Corolla', 2020)
print(car1.get_descriptive_name())
print(f"Vehicle Type: {car1.vehicle_type}")
print("Odometer Reading:")
car1.read_odometer()