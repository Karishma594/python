from logging import setLoggerClass

from tornado.web import TemplateModule


class Mathops:
    @staticmethod
    def is_even(num):
        return num%2==0
print(Mathops.is_even(8))
obj=Mathops()
print(obj.is_even(5))

class Student:
    total_students = 0

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
        Student.total_students += 1

    def is_passed(self):
        if self.marks > 40:
            return "Pass"
        else:
            return "Fail"


s1 = Student("karishma", 45)
s2 = Student("shameena", 35)

print("Total Students:", Student.total_students)

class Employee:
    company_name="TechCorp"
    def __init__(self,name):
        self.name=name
    @classmethod
    def change_company(cls,new_name):
        cls.company_name=new_name
e1=Employee("karishma")
Employee.change_company("Infotech")
print(e1.name,e1.company_name)

class Car:
    wheels=4
    def __init__(self,mileage):
        self.mileage=mileage
    def display_specs(self):
        print(f"mileage:{self.mileage}")
        print(f"wheels:{self.wheels}")
    @classmethod
    def change_wheels(cls,new_wheels):
        cls.wheels=new_wheels
c1=Car(35)
c1.display_specs()
Car.change_wheels(5)
c1.display_specs()

class Temperature:
    def __init__(self,celsius):
        self.celsius=celsius
    @staticmethod
    def to_fahrenheit(celsius):
        return (celsius*9/5)+32
    def show_conversion(self):
        print("celsius:",self.celsius)
        print("fahrenheit:",Temperature.to_fahrenheit(self.celsius))
t1=Temperature(20)
t1.show_conversion()

class Book:
    total_books=0
    def __init__(self,title,author):
        self.title=title
        self.author=author
        Book.total_books+=1
    @classmethod
    def from_string(cls,book_str):
        title,author=book_str.split("-")
        return cls(title,author)
    @staticmethod
    def is_valid_title(title):
        return len(title)>=3
if Book.is_valid_title("python"):
    b1=Book("python","guido")
b2=Book.from_string("java-james")
print("Total Books:",Book.total_books)


class Employee:
    bonus_rate=0.1
    def __init__(self,name,base_salary):
        self.name=name
        self.base_salary=base_salary
    def final_salary(self):
        return self.base_salary+(self.base_salary*Employee.bonus_rate)
    @classmethod
    def update_bonus(cls,new_rate):
        cls.bonus_rate=new_rate
    @staticmethod
    def is_valid_salary(sal):
        return sal>0
e1=Employee("karishma",30000)
e2=Employee("shameena",7000)
print(e1.final_salary())
print(e2.final_salary())
Employee.update_bonus(2)
print(e1.final_salary())
print(e2.final_salary())

class Course:
    total_students=0
    def __init__(self,student_name):
        self.student_name=student_name
    def enroll(self):
        Course.total_students+=1
    @classmethod
    def show_total(cls):
        print("Total students:",Course.total_students)
    @staticmethod
    def is_eligible(age):
        return age>=18
c1=Course("karishma")
c2=Course("Zoya")
c1.enroll()
c2.enroll()
Course.show_total()
print(Course.is_eligible(17))

class BankAccount:
    bank_name="SBI"
    def __init__(self,holder,balance):
        self.holder=holder
        self.balance=balance
    def deposit(self,amount):
        if BankAccount.validate_amount(amount):
            self.balance+=amount
            print("Deposit:",amount)
    @classmethod
    def change_bank_name(cls,new_name):
        cls.bank_name=new_name
    @staticmethod
    def validate_amount(amount):
        return amount>0
acc1=BankAccount("zoya",100000)
acc1.deposit(10000)
print("Balance:",acc1.balance)
BankAccount.change_bank_name("HDFC")
print("New Bank Name:",BankAccount.bank_name)


class Student:
    passing_marks=40
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def result(self):
        if self.marks>Student.passing_marks:
            print(self.name,"pass")
        else:
            priint(self.name,"fail")
    @classmethod
    def updating_passing_marks(cls,new_marks):
        cls.passing_marks=new_marks
    @staticmethod
    def grade_category(marks):
        if marks>=90:
            return "A"
        elif marks>=50:
            return "B"
        else:
            return "C"
s1=Student("shakeela",50)
Student.updating_passing_marks(30)
print(s1.grade_category(60))