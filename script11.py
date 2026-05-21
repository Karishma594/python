class E:
    def __init__(self,a):
        self.a=a
    def __gt__(self,o2):
        return self.a>o2.a
    def __lt__(self,o2):
        return self.a<o2.a
    def __ge_(self,o2):
        return self.a>o2.a
    def __le__(self,o2):
        return self.a<o2.a
    def __eq__(self,o2):
        return self.a==o2.a
e1=E(27)
e2=E(27)
print(e1>e2)
print(e1<e2)
print(e1>=e2)
print(e2<=e1)
print(e1==e2)


class Vector:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def td(self):
        return (self.x**2+self.y**2)**(1/2)
    def __add__(self,o2):
        return self.x+o2.x,self.y+o2.y
    def __sub__(self,o2):
        return self.x-o2.x,self.y-o2.y
    def __ge__(self,o2):
        return self.td()>o2.td()
    def _ge__(self, o2):
        return self.td() > o2.td()





