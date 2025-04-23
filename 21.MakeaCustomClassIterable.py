# 21. Make a Custom Class Iterable
# Create a class Countdown that takes a start number. Implement __iter__() and __next__() to make the object iterable in a for-loop, counting down to 0.

class Countdown:
    def __init__(self, start):
        self.current = start  

    def __iter__(self):
        return self 
    def __next__(self):
        if self.current < 0:
            raise StopIteration  
        value = self.current
        self.current -= 1
        return value

# Test the iterable
for number in Countdown(9):
    print(number)


# 🗣️ Explanation:
# 1.__init__ Method:
# Start number set karta hai (e.g., 5 se start hoga).

# 2.__iter__() Method:
# Apne aap ko return karta hai, kyunki ye object hi iterator bhi hai.
 
# 3.__next__() Method:
# Har call pe ek number return karta hai aur current value ko kam karta hai.
# Jab number 0 se neeche jaye, StopIteration raise hoti hai (loop khatam).


