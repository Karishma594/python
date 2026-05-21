from setuptools import namespaces


class Student:
    passing_marks=40
    def __init__(self,name,marks):
            self.name=name
            self.marks=marks
    def result(self):
        if self.marks>=Student.passing_marks:
            print(self.name,"pass")
        else:
            print(self.name,"fail")
    @classmethod
    def update_passing_marks(cls,new_marks):
        cls.new_marks=new_marks
    @staticmethod
    def grade_category(marks):
        if marks>=75:
            return "A"
        elif marks>=50:
            return "B"
        else:
            return "C"
s1=Student("kavi",75)
s2=Student("zoya",34)
s1.result()
s2.result()
Student.update_passing_marks(70)
s1.result()
s2.result()
print(Student.grade_category(s1.marks))
print(Student.grade_category(s2.marks))

# Q6. Book Class

class Book:
    total_books = 0

    def __init__(self, title, author):
        self.title = title
        self.author = author
        Book.total_books += 1

    @classmethod
    def from_string(cls, book_str):
        title, author = book_str.split("-")
        return cls(title, author)

    @staticmethod
    def is_valid_title(title):
        return len(title) >= 3


if Book.is_valid_title("Python"):
    b1 = Book("Python", "Guido")

if Book.is_valid_title("Java"):
    b2 = Book.from_string("Java-James")

print("Total Books:", Book.total_books)



class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def is_passed(self):
        if self.marks>40:
            return "pass"
        else:
            return "Fail"
s1=Student("shameena",45)
s2=Student("zoya",87)
print(s1.is_passed())
print(s2.is_passed())


class Employee:
    company_name="Techcorp"
    def __init__(self,name):
        self.name=name
    @classmethod
    def change_company(cls,new_name):
        cls.company_name=new_name
e1=Employee("kari")
e2=Employee("shaki")
print(e1.company_name)
print(e2.company_name)
Employee.change_company("tech")
print(e1.company_name)
print(e2.company_name)


class Employee:
    min_experience = 2
    valid_departments = ["HR", "Tech", "Admin"]

    def __init__(self, name, experience, dept):
        self.name = name
        self.experience = experience
        self.dept = dept

    def promotion_eligible(self):
        return self.experience >= Employee.min_experience

    @classmethod
    def update_criteria(cls, years):
        cls.min_experience = years

    @staticmethod
    def is_valid_department(dept):
        return dept in Employee.valid_departments


# Demo
e1 = Employee("Asha", 3, "Tech")
e2 = Employee("John", 1, "HR")

print(e1.promotion_eligible(), Employee.is_valid_department(e1.dept))
print(e2.promotion_eligible(), Employee.is_valid_department(e2.dept))

Employee.update_criteria(4)

print(e1.promotion_eligible())
