# 8. The super() Function
# Create a class Person with a constructor that sets the name. Inherit a class Teacher from it, add a subject field, and use super() to call the base class constructor.

class Person:
    def __init__(self, name):
        self.name = name
        print(f"Person initialized with name: {self.name}")

class Teacher(Person):
    def __init__(self, name, subject):
        super().__init__(name)  # Calling the base class constructor
        self.subject = subject
        print(f"Teacher initialized with subject: {self.subject}")

# Example usage:
t1 = Teacher("Mr. Ather", "Mathematics")
