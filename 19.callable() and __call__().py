# 19. callable() and __call__()
# Create a class Multiplier with an __init__() to set a factor. Define a __call__() method that multiplies an input by the factor. Test it with callable() and by calling the object like a function.

# 💻 Code:
class Multiplier:
    def __init__(self, factor):
        self.factor = factor

    def __call__(self, number):
        return number * self.factor

# Create object
double = Multiplier(2)

# Test callable
print(callable(double))  # Output: True

# Call the object like a function
result = double(4)
print(result)  


# ✅ Summary (Roman Urdu):
# Jab kisi object me __call__() method hota hai, to tum usay function ki tarah use kar sakte hain.

# Ye feature tab kaam aata hai jab tum chahte ho ke object behave kare jaise ek function, but uske andar kuch state (jaise factor) bhi ho.