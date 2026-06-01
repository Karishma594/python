class UPI:
    def pay(self,mpin):
        print("UPI")
class Card:
    def pay(self,pin,otp):
        print("Card")
class Cash:
    def pay(self,amount):
        print("Cash")
    def payment(x):
        if isinstance(x,UPI):
            x.pay(1787)
        elif isinstance(x,cash):
            x.pay(8000)
        elif isinstance(x,Card):
            x.pay(A87,5087)
        else:
            print("Wrong choice")
c1=Card()
c2=Cash()
c3=UPI()
payment(1)
payment(2)
payment(3)


class Animal:
    def make_sound(self):
        print("Making Sound")
class Dog:
    def make_sound(self):
        print("Bow Bow")
class Cat:
    def make_sound(self):
        print("Meow Meow")
class Cow:
    def make_sound(self):
        print("Moo Moo")
Animal=[Dog(),Cat(),Cow()]
for i in Animal:
    i.make_sound()


def operate(device):
    device.start()
class Car:
    def start(self):
        print("Car")
class Computer:
    def start(self):
        print("Computer")
class WashingMachine:
    def start(self):
        print("Washing Machine")
operate(Car())
operate(Computer())
operate(WashingMachine())


