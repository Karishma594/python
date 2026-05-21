class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount

    def __str__(self):
        return f"{self.account_holder}: {self.balance}"

    def __add__(self, o2):
        return self.balance + o2.balance

    def __sub__(self, other):
        return self.balance - other.balance

    def __eq__(self, other):
        return self.balance == other.balance

    def __lt__(self, other):
        return self.balance < other.balance

    def __getattribute__(self, name):
        print(f"Accessing {name}")
        return super().__getattribute__(name)

    def __setattr__(self, name, value):
        if name == "balance" and value < 0:
            print("Negative balance not allowed")
        super().__setattr__(name, value)


a1 = BankAccount("Karishma", 5000)
a2 = BankAccount("Shaik", 3000)

print(a1 + a2)
print(a1 - a2)
print(a1 == a2)
print(a1 < a2)

class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def total_price(self):
        return self.price * self.quantity

    def __str__(self):
        return f"{self.name}: {self.total_price()}"

    def __add__(self, other):
        return self.total_price() + other.total_price()

    def __mul__(self, o2):
        return self.total_price()* o2.total_price()

    def __gt__(self, other):
        return self.total_price() > other.total_price()

    def __eq__(self, other):
        return self.price == other.price

    def __getattr__(self, name):
        return "Attribute not found"

    def __setattr__(self, name, value):
        if name == "price" and value < 0:
            raise ValueError("Invalid price")
        super().__setattr__(name, value)
p1=Product("karishma",20,5)
p2=Product("zoya",30,5)
print(p1+p2)
print(p1*p2)
print(p1>p2)

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def grade(self):
        return "Pass" if self.marks >= 40 else "Fail"

    def __str__(self):
        return f"{self.name}: {self.marks}"

    def __add__(self, other):
        return self.marks + other.marks

    def __truediv__(self,o2):
        return self.marks /o2.marks

    def __ge__(self, other):
        return self.marks >= other.marks

    def __lt__(self, other):
        return self.marks < other.marks

    def __getattribute__(self, name):
        print(f"Accessing {name}")
        return object.__getattribute__(self, name)

    def __setattr__(self, name, value):
        if name == "marks" and not (0 <= value <= 100):
            raise stopiteration
        print("Marks must be 0-100")
        super().__setattr__(name, value)

s1=Student("karishma",40)
s2=Student("shameena",90)
print(s1+s2)
print(s1/s2)
print(s1>=s2)
print(s1<s2)