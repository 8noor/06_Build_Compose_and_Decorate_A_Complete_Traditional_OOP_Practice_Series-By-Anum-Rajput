# 6. Constructors and Destructors
# Create a class Logger that prints a message when an object is created (constructor) and another message when it is destroyed (destructor).

# Solution
class Logger:
    def __init__(self):
        print("Logger initialized: Object created.")

    def __del__(self):
        print("Logger finalized: Object destroyed.")

# Example usage:
log = Logger()

# Manually deleting the object (for demonstration)
del log
