class Product:
    def __init__(self,name,price,quantity):
        self.name=name
        self.price=price
        self.quantity=quantity
    def __str__(self):
        return f"Product Name:{self.name}\nprice:{self.price}\nquantity:{self.quantity}"
class Cart:
    def __init__(self):
        self.l=[]
    def __add__(self,o2):
        self.l.append(o2)
        return self
    def __sub__(self,o2):
        if o2 in self.l:
            self.l.remove(o2)
    def total_price(self):
        s=0
        for i in self.l:
            st=(i.price*i.quantity)
        return s
    def __str__(self):
        for i in self.l:
            print(i)
        print(f"total products:{len(self.l)}")
        print("total price:{self.total_price()}")

class E:
    def __init__(self,a):
        self.a=a
    def __gt__(self,o2):
        return self.a>o2.a
e1=E(20)
e2=E(17)



