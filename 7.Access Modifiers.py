# 7. Access Modifiers: Public, Private, and Protected
# Create a class Employee with:

# a public variable name,

# a protected variable _salary, and

# a private variable __ssn.

# Try accessing all three variables from an object of the class and document what happens.

# Solution
class Employee:
    def __init__(self, name, salary, ssn):
        self.name = name         # Public variable
        self._salary = salary    # Protected variable
        self.__ssn = ssn         # Private variable

# Creating an object
emp = Employee("Ather", 75000, "123-27-13715")

# Accessing public variable
print("Public - Name:", emp.name)

# Accessing protected variable
print("Protected - Salary:", emp._salary)

# Accessing private variable directly (will raise AttributeError)
try:
    print("Private - SSN:", emp.__ssn)
except AttributeError as e:
    print("Private - SSN: Cannot access directly! Error:", e)

# Accessing private variable using name mangling
print("Private (via name mangling) - SSN:", emp._Employee__ssn)
