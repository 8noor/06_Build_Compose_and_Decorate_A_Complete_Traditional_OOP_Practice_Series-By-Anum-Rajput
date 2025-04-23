# 5. Static Variables and Static Methods
# Create a class MathUtils with a static method add(a, b) that returns the sum. No class or instance variables should be used.

# Solution
class MathUtils:
    @staticmethod
    def add(a, b):
        return a + b  # Simply return the sum

# Example usage:
result = MathUtils.add(8, 9)
print("Sum:", result)
