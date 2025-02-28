class Vehicle:
    def __init__(self, brand, model, year, rental_price_per_day):
        self.brand = brand
        self.model = model
        self.year = year
        self._rental_price_per_day = rental_price_per_day

    def display_info(self):
        print(f"Brand: {self.brand}, Model: {self.model}, Year: {self.year}, Rental Price: ${self._rental_price_per_day}/day")

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
        super().display_info()
        print(f"Seats: {self.seating_capacity}")


class Bike(Vehicle):
    def __init__(self, brand, model, year, rental_price_per_day, engine_capacity):
        super().__init__(brand, model, year, rental_price_per_day)
        self.engine_capacity = engine_capacity

    def display_info(self):
        super().display_info()
        print(f"Engine: {self.engine_capacity}cc")


class RentalSystem:
    def __init__(self):
        self.vehicles = []

    def add_vehicle(self, vehicle):
        self.vehicles.append(vehicle)

    def display_vehicles(self):
        for vehicle in self.vehicles:
            vehicle.display_info()

    def rent_vehicle(self, vehicle, days):
        print(f"Rental cost for {vehicle.brand} {vehicle.model} for {days} days: ${vehicle.calculate_rental_cost(days)}")

    def update_rental_price(self, vehicle, price):
        vehicle.set_rental_price(price)
        print(f"Updated rental price for {vehicle.brand} {vehicle.model}: ${vehicle.get_rental_price()}/day")


def main():
    rental_system = RentalSystem()

    car = Car("Toyota", "Corolla", 2020, 50, 5)
    bike = Bike("Yamaha", "R1", 2019, 30, 998)

    rental_system.add_vehicle(car)
    rental_system.add_vehicle(bike)

    print("Available Vehicles:")
    rental_system.display_vehicles()

    rental_system.rent_vehicle(car, 3)
    rental_system.rent_vehicle(bike, 5)

    rental_system.update_rental_price(car, 55)


if __name__ == "__main__":
    main()