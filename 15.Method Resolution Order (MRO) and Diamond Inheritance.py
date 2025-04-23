# 15. Method Resolution Order (MRO) and Diamond Inheritance
# Create four classes:

# A with a method show(),
# B and C that inherit from A and override show(),
# D that inherits from both B and C.
# Create an object of D and call show() to observe MRO.

# 🔷 Concept: Diamond Inheritance

#       A
#      / \
#     B   C
#      \ /
#       D

# A base class hai.
# B aur C dono A se inherit karte hain.
# D class, B aur C dono se inherit karti hai.

# 💻 Code:
class A:
    def show(self):
        print("Show from A")

class B(A):
    def show(self):
        print("Show from B")

class C(A):
    def show(self):
        print("Show from C")

class D(B, C):  # Inheriting from B and C
    pass

# Object of class D
obj = D()
obj.show()

# Print MRO
print(D.__mro__)

# 🤓Method Resolution Order (MRO).
# Python ne pehle D dekha — koi show() method nahi tha.
# Phir B dekha — usme show() mil gaya — isi liye wahi run hua.
# Agar B mein na milta to C, phir A check karta.
# MRO decide karta hai Python ke rules ke mutabiq — usually left to right inheritance ke order mein.