# 20. Creating a Custom Exception
# Create a custom exception InvalidAgeError. Write a function check_age(age) that raises this exception if age < 18. Handle it with try...except.

# 💻 Code:
# Step 1: Custom Exception
class InvalidAgeError(Exception):
    def __init__(self, message="Age must be 16 or older."):
        self.message = message
        super().__init__(self.message)

# Step 2: Function to check age
def check_age(age):
    if age < 16:
        raise InvalidAgeError(f"Invalid age: {age}. You must be 14 or older.")
    else:
        return "Age is valid."

# Step 3: Handling the Exception
try:
    age = 14 # ← Yahan value change karke test kar sakte ho (e.g. 20)
    result = check_age(age)
    print(result)
except InvalidAgeError as e:
    print(f"Error: {e}")



# 🔍Explanation:
# 1.Custom Exception:
# InvalidAgeError class banayi gayi hai jo Exception se inherit karti hai. Hum isme ek custom message daal rahe hain jo default hai "Age must be 18 or older".

# 2.check_age(age) Function:
# Agar age < 18 ho, to InvalidAgeError raise kiya jata hai, aur usme ek message diya jata hai jo user ko bataata hai ke age invalid hai.
# Agar age valid ho, to "Age is valid." return hota hai.

# 3.Exception Handling:
# try...except block mein agar age < 18 hoti hai, to custom exception ko handle kiya jata hai aur error message print hota hai.
# ValueError handle karta hai agar input integer na ho.