class Character:
    def __init__(self,name,hp,attack,buff=0.2):
        self.name=name
        self.hp=hp
        self.attack=attack
        self.buff=buff
    def __str__(self):
        return f"name:{self.name}\n hp:{self.hp}\n attack:{self.attack}\n buff:{self.buff}"
    def __repr__(self):
        return str(self)
class Mage(Character):
    pass
class Warrior(Character):
    pass
m1=Mage("Santhi",100,20,0.3)
w1=Warrior("Manisha",100,30,0.4)
print(m1.__str__())
print(w1.__str__())
print(m1.__repr__())
print(w1.__repr__())



