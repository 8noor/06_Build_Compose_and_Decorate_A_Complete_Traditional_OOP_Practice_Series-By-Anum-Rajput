# 4.Class Variables and Class Methods
# Assignment:
# Create a class Bank with a class variable bank_name. Add a class method change_bank_name(cls, name) that allows changing the bank name. Show that it affects all instances.
# Solution

class Bank:
    bank_name = "HBL Bank"  # Class variable

    def __init__(self, account_holder):
        self.account_holder = account_holder

    @classmethod
    def change_bank_name(cls, name):
        cls.bank_name = name  # Modifying the class variable

    def display(self):
        print(f"Account Holder: {self.account_holder}, Bank: {Bank.bank_name}")

# Create instances
acc1 = Bank("Ali")
acc2 = Bank("Ather")

# Display initial bank names
acc1.display()  # Default Bank
acc2.display()  # Default Bank

# Change the bank name using class method
Bank.change_bank_name("Global Trust Bank")

# Display after change - should reflect for all instances
acc1.display()  # Global Trust Bank
acc2.display()  # Global Trust Bank
