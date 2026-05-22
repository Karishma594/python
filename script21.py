class A:
    x=0
    def m1(self):
        print("A Class")
class B(A):
    pass
b1=B()
class C:
    def m1(self):
        a1=A()
        a1.m1()
c1=C()
c1.m1()