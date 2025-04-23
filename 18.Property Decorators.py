# 18. Property Decorators: @property, @setter, and @deleter
# Create a class Product with a private attribute _price. Use @property to get the price, @price.setter to update it, and @price.deleter to delete it.

# 💻 Code:
class Product:
    def __init__(self, price):
        self._price = price  # Private attribute

    @property
    def price(self):
        print("Getting price...")
        return self._price

    @price.setter
    def price(self, value):
        print("Setting price...")
        if value >= 0:
            self._price = value
        else:
            raise ValueError("Price cannot be negative.")

    @price.deleter
    def price(self):
        print("Deleting price...")
        del self._price

# Test
p = Product(55000)

print(p.price)      # Getter
p.price = 84000       # Setter
print(p.price)

del p.price         # Deleter
