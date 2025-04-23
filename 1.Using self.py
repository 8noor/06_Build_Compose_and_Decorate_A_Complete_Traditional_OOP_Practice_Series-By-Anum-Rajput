# 06_Build_Compose_and_Decorate_A_Complete_Traditional_OOP_Practice_Series

# 1. Using self
# Assignment:
# Create a class Student with attributes name and marks. Use the self keyword to initialize these values via a constructor. Add a method display() that prints student details.

# Solution

class Student:
    def __init__(self, name, marks):
        self.name = name      # Initializing name using self
        self.marks = marks    # Initializing marks using self

    def display(self):
        print("Student Name:", self.name)
        print("Marks:", self.marks)

# Example usage:
student1 = Student("Alice", 92)
student1.display()
