class A:
    def m1(self):
        print("A Class")
class B(A):
    def m1(self):
        print("B")
        super().m1()
b1=B()
b1.m1()
a1=A()
a1.m1()


class A:
    def m1(self):
        print("A")
class B:
    def m1(self):
        print("B")
        super().m1()
class C:
    def m1(self):
        print("C")
        super().m1()
class D(A,B,C):
    def m1(self):
        print("D")
        super().m1()
d1=D()
d1.m1()
D.mro()

class A:
    def m1(self):
        print("A")
class B:
    def m1(self):
        super().m1()
        print("B")
class C:
    def m1(self):
        super().m1()
        print("C")
class D(A,B,C):
    def m1(self):
        super().m1()
        print("D")
d1=D()
d1.m1()

