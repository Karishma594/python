class HotelRoom:
    base_price=500
    total_bill=0
    def __init__(self,room_no,nights_booked,guest_name):
        self.room_no=room_no
        self.nights_booked=nights_booked
        self.guest_name=guest_name
    @classmethod
    def calculate_total_bill(cls,base_price):
        base_price+=500
        total_bill=base_price*nights_booked
    @staticmethod
    def is_valid(nights_booked):
        if nights_booked>5:
            return 0
HotelRoom(204,3,"karishma")
print(HotelRoom)

class Product:
    total_products=0
    def __init__(self,name,category,price,quantity):
        self.name=name
        self.category=category
        self.price=price
        self.quantity=quantity
        total_products+=1
    @classmethod
    def from_string(cls,product_str):
        Product.name_category_price_quantity

    def is_valid_price(self,price):
        if price>0:
            return 0

class Books:
    def __init__(self,title,author,is_borrowed):
        self.title=title
        self.author=author
        self.is_borrowed=is_borrowed
    def __str__(self):
        return f"{self.title}:{self.author}"
    def __repr__(self):
        return f"{self.title}:{self.author}""
class Library:
    l={}
    def __add__(self,o2):
        if len(o2.title)>7:
            Library[o2.title]=o2
            return Library.l
        else:
            return "length of title is short"

def  func():
    if sub<=0:
        return 0
@dec
def subtraction():
    def Inner():
        sub=x-y
        return sub
    return Inner
func(9,13)






