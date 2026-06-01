class A:
    _x=30
class B(A):
    def m1(self):
        print(self._x)
print(A._x)


class C:
    def __init__(self):
        self.__y=30
class D(C):
    def m1(self):
        pass
c1=C()
print(c1._C__y)

class Bank:
    def __init__(self,AccNo,balance,pin,name):
        self.AccNo=AccNo
        self.__balance=balance
        self.__pin=pin
        self._name=name
    def Withdraw(self,amount):
        if amount<=self.__balance:
            self.__balance-=amount
            print("Withdrawn Successfully")
        else:
            print("Invalid amount")
    def deposit(self,amount):
        if amount>=0:
            self.__balance+=amount
        else:
            print("Invalid amount")
    def display(self):
        p=input("Enter pin:")
        if p==self.__pin:
            print(f"balance:{self.__balance}")
b1=Bank(35204,2000,1594,"karishma")
b1.deposit(10000)
b1.Withdraw(1000)
b1.display()

class A:
    def __init__(self,a):
        self._x=a
        self.__y=50
    @property
    def Z(self):
        return self._x
    def Z(self,nx):
        self._x=nx
a1=A(10)
a1.z=30



