def dec(x):
    def Inner():
        print("Start")
        x()
        print("End")
    return Inner
@dec
def greet():
    print("Hello")
greet()

def dec(fun):
    def Inner(name):
        print("Start")
        fun(name)
        print("Done")
    return Inner
@dec
def greet(name):
    print("Hello",name)
greet("Ravi")

def dec(func):
    def Inner():
        result = func()
        return result * 2
    return Inner

@dec
def number():
    return 25
print(number())

user_role="Student"
def dec(func):
    def Inner():
        if user_role=="Admin":
            func()
        else:
            print("Access Denied")
    return Inner
@dec
def show():
    print("Welcome Admin")
show()


def upper(func):
    def inner():
        return func().upper()
    return inner
@upper
def get_msg():
    return "hello world"
print(get_msg())

