class A:
    def __init__(self,x):
        self.x=x
    def __add__(self,o2):
        return self.x+o2


class B:
    def __init__(self,x):
        self.x=x
    def __add__(self,o2):
        return self.x+o2.x
b1=B(30)
b2=B(35)
print(b1+b2)


class B:
    def __init__(self,x):
        self.x=x
    def __add__(self,o2):
        if isinstance(o2,int):
            return self.x+o2
        if isinstance(o2,B):
            return self.x+o2.x
        else:
            print("Wrong Class")
            return 0
b1=B(30)
b2=B(35)
print(b1+b2)
print(b1+45)


class C:
    def __init__(self,x,y,z):
        self.x=x
        self.y=y
        self.z=z
    def __add__(self,o2):
        if isinstance(o2,str):
            return self.x+o2
        elif isinstance(o2,int):
            return self.y+o2
        else:
            return self.z+o2.z
c1=C("Hi",20,30)
c2=C("Hello",30,40)
print(c1+"Hello")
print(c1+75)
print(c1+c2)

class D:
    def __str__(self):
        return "This D Class"
    def __repr__(self):
        return "This is repr"
d1=D()
print(d1)
print(str(d1))
print([d1])
print(str([d1]))

class E:
    def __init__(self,x,y,z):
        self.x=x
        self.y=y
        self.z=z
    def __str__(self):
        return f"x:{self.x}\ny:{self.y}\nz:{self.z}"
    def __repr__(self):
        return f"x:{self.x}\ny:{self.y}\nz:{self.z}"
e1=E(20,30,40)
print(e1)