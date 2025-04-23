# 14. Aggregation
# Create a class Department and a class Employee. Use aggregation by having a Department object store a reference to an Employee object that exists independently of it.

# 📘 Concept: Aggregation
# Aggregation ka matlab hai ke aik class doosri class ka reference rakhti hai, lekin dono objects independently exist karte hain.

# Jaise:
# Employee pehle se bana hua hai.
# Department sirf uska reference rakhta hai — agar Department delete ho jaye, Employee phir bhi zinda rahega.

# 💻 Code Example:
class Employee:
    def __init__(self, name):
        self.name = name

    def get_details(self):
        return f"Employee: {self.name}"

class Department:
    def __init__(self, name, employee):
        self.name = name
        self.employee = employee  

    def show_department_info(self):
        return f"Department: {self.name}, {self.employee.get_details()}"


emp1 = Employee("Saeed")


dept = Department("HR", emp1)

# Department se employee ki info dikhayi
print(dept.show_department_info())  

# 🧠 Summary!
# Aggregation mein aik object (jaise Employee) doosri class mein sirf reference ke tor par hota hai.

# Dono alag alag zindagi guzarte hain — ek ka marna doosray ko affect nahi karta 😄