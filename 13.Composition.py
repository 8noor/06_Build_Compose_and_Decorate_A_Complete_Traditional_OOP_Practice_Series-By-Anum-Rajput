# 13. Composition
# Create a class Engine and a class Car. Use composition by passing an Engine object to the Car class during initialization. Access a method of the Engine class via the Car class.

# ✅ Composition Concept:
# Composition is when one class contains an instance of another class.
# In this case, a Car has an Engine.

# 📘 Concept: Composition
# Composition ka matlab hota hai ke aik class ke andar doosri class ka object use kiya jaye.

# Jaise:
# Car ke paas aik Engine hota hai.
# To hum Car class ke andar Engine ka object pass karte hain.

# 🧱 Example Code:
class Engine:
    def start(self):
        return "Engine started."

class Car:
    def __init__(self, engine):
        self.engine = engine  

    def start_car(self):
        return self.engine.start()  

# Create an Engine object
my_engine = Engine()

# Pass the Engine object to the Car
my_car = Car(my_engine)

# Call the Car's method that uses Engine's method
print(my_car.start_car()) 
