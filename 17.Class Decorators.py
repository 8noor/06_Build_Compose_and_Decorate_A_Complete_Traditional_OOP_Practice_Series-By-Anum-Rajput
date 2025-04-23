# 17. Class Decorators
# Create a class decorator add_greeting that modifies a class to add a greet() method returning "Hello from Decorator!". Apply it to a class Person.

# 💻 Code:
# Class decorator
def add_greeting(cls):
    def greet(self):
        return "Hello from Decorator!"
    cls.greet = greet  # Dynamically adding the method to the class
    return cls

# Apply the decorator to Person class
@add_greeting
class Person:
    def __init__(self, name):
        self.name = name

# Test
p = Person("Anum")
print(p.greet())  # Output: Hello from Decorator!

# 🔍🧠Explanation:
# add_greeting(cls) ek function hai jo class ko accept karta hai.
# Is function ke andar hum greet() method define karte hain.
# Phir cls.greet = greet likh kar hum ye method us class me add kar dete hain.
# Jab @add_greeting lagate hain Person class par, to greet() method us class ka part ban jaata hai.

