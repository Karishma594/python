class Car:
    fuel_type="petrol"
    def __init__(self,model,year,price):
        self.model=model
        self.year=year
        self.price=price
    def display(self):
        print("model:",self.model,"year:",self.year,"price:",self.price)
c1=Car("BMW",2026,10000000)
c2=Car("KIA",2025,200000)
c1.display()
c2.display()


class Employee:
    employee_count=0
    def __init__(self):
        Employee.employee_count+=1
e1=Employee()
e2=Employee()
e3=Employee()
e4=Employee()
print(Employee.employee_count)

class Student:
    def __init__(self,name,age,gpa):

