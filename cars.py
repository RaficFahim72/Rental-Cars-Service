class Vehicle:
    def __init__(self, brand, model, year, rental_price_per_day):
        self.brand = brand
        self.model = model
        self.year = year
        self._rental_price_per_day = rental_price_per_day  # Private attribute

    def display_info(self):
        print(f"🚗 Vehicle: {self.brand} {self.model}, Year: {self.year}, Rental Price: ${self._rental_price_per_day}/day")

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
        print(f"🪑 Seats: {self.seating_capacity}")


class Bike(Vehicle):
    def __init__(self, brand, model, year, rental_price_per_day, engine_capacity):
        super().__init__(brand, model, year, rental_price_per_day)
        self.engine_capacity = engine_capacity

    def display_info(self):
        super().display_info()
        print(f"🏍️ Engine: {self.engine_capacity}cc")


class VehicleRentalSystem:
    def __init__(self):
        self.vehicles = []

    def add_vehicle(self, vehicle):
        self.vehicles.append(vehicle)

    def display_vehicles(self):
        print("\n🌟 Available Vehicles:")
        for idx, vehicle in enumerate(self.vehicles):
            print(f"{idx + 1}. ", end="")
            vehicle.display_info()

    def rent_vehicle(self, index, days):
        if 0 <= index < len(self.vehicles):
            vehicle = self.vehicles[index]
            cost = vehicle.calculate_rental_cost(days)
            print(f"\n🎉 You have successfully rented the {vehicle.brand} {vehicle.model} for {days} days!")
            print(f"💰 Total rental cost: ${cost}. Enjoy your ride!")
        else:
            print("🚫 Oops! That vehicle selection is invalid. Please try again.")

    def update_rental_price(self, index, new_price):
        if 0 <= index < len(self.vehicles):
            vehicle = self.vehicles[index]
            vehicle.set_rental_price(new_price)
            print(f"✅ Updated rental price for {vehicle.brand} {vehicle.model}: ${vehicle.get_rental_price()}/day")
        else:
            print("🚫 Oops! That vehicle selection is invalid. Please try again.")


def main():
    rental_system = VehicleRentalSystem()

    # Create instances of Car and Bike
    car1 = Car("Toyota", "Corolla", 2020, 50, 5)
    bike1 = Bike("Yamaha", "R1", 2019, 30, 998)

    # Add vehicles to the rental system
    rental_system.add_vehicle(car1)
    rental_system.add_vehicle(bike1)

    print("👋 Welcome to the Vehicle Rental System! Let's get you on the road!")

    while True:
        print("\n--- Vehicle Rental System Menu ---")
        print("1. View Available Vehicles")
        print("2. Rent a Vehicle")
        print("3. Update Rental Price")
        print("4. Exit")
        choice = input("Please enter your choice (1-4): ")

        if choice == '1':
            rental_system.display_vehicles()
        elif choice == '2':
            rental_system.display_vehicles()
            vehicle_index = int(input("Select the vehicle number you want to rent: ")) - 1
            rental_days = int(input("How many days would you like to rent it for? "))
            rental_system.rent_vehicle(vehicle_index, rental_days)
        elif choice == '3':
            rental_system.display_vehicles()
            vehicle_index = int(input("Select the vehicle number you want to update the price for: ")) - 1
            new_price = float(input("Enter the new rental price: "))
            rental_system.update_rental_price(vehicle_index, new_price)
        elif choice == '4':
            print("👋 Thank you for using the Vehicle Rental System! Safe travels!")
            break
        else:
            print("🚫 Invalid choice. Please try again.")

if __name__ == "__main__":
    main()