class Vehicle:
    def __init__(self, brand, model, year, rental_price_per_day):
        self.brand = brand
        self.model = model
        self.year = year
        self._rental_price_per_day = rental_price_per_day  # Private attribute

    def display_info(self):
        print(f"Vehicle: {self.brand} {self.model}, Year: {self.year}, Rental Price: ${self._rental_price_per_day}/day")

    def calculate_rental_cost(self, days):
        return self._rental_price_per_day * days

    def set_rental_price(self, price):
        self._rental_price_per_day = price

    def get_rental_price(self):
        return self._rental_price_per_day


class Car(Vehicle):
    def __init__(self, brand, model, year, rental_price_per_day, seating_capacity):
        super().__init__(brand, model, year, rental_price_per_day)
        self.seating_capacity = seating_capacity

    def display_info(self):
        print(f"Car: {self.brand} {self.model}, Year: {self.year}, Seats: {self.seating_capacity}, Rental Price: ${self._rental_price_per_day}/day")


class Bike(Vehicle):
    def __init__(self, brand, model, year, rental_price_per_day, engine_capacity):
        super().__init__(brand, model, year, rental_price_per_day)
        self.engine_capacity = engine_capacity

    def display_info(self):
        print(f"Bike: {self.brand} {self.model}, Year: {self.year}, Engine: {self.engine_capacity}cc, Rental Price: ${self._rental_price_per_day}/day")


def show_vehicle_info(vehicle):
    vehicle.display_info()


# Create instances of Car and Bike
car = Car("Toyota", "Corolla", 2020, 50, 5)
bike = Bike("Yamaha", "R1", 2019, 30, 998)

# Display their details
show_vehicle_info(car)
show_vehicle_info(bike)

# Calculate rental costs for a given number of days
rental_days_car = 3
rental_days_bike = 5
print(f"Rental cost for {car.brand} {car.model} for {rental_days_car} days: ${car.calculate_rental_cost(rental_days_car)}")
print(f"Rental cost for {bike.brand} {bike.model} for {rental_days_bike} days: ${bike.calculate_rental_cost(rental_days_bike)}")

# Modify rental prices using setter methods and display the updated price
car.set_rental_price(55)
print(f"Updated rental price for {car.brand} {car.model}: ${car.get_rental_price()}/day")