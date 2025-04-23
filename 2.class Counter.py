# 2. Using cls
# Assignment:
# Create a class Counter that keeps track of how many objects have been created. Use a class variable and a class method with cls to manage and display the count.

# Solution
class Counter:
    count = 0  # Class variable to keep track of number of objects

    def __init__(self):
        Counter.count += 1  # Increment count whenever a new object is created

    @classmethod
    def display_count(cls):
        print("My total created objects are:", cls.count)

# Example usage:
obj1 = Counter()
obj2 = Counter()
obj3 = Counter()
obj4 = Counter()
obj5 = Counter()

Counter.display_count()  # Output: Total objects created: 3

