# 3.Public Variables and Methods
# Assignment:
# Create a class Car with a public variable brand and a public method start(). Instantiate the class and access both from outside the class.

# Solution
class Car:
    def __init__(self, brand):
        self.brand = brand  # Public variable

    def start(self):  # Public method
        print(f"{self.brand} car is starting...!")

# Instantiate the class
my_car = Car("Toyota")

# Accessing public variable
print("Car Brand:", my_car.brand)

# Calling public method
my_car.start()
