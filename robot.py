#from dinosaur import Dinosaur
from weapon import Weapon
class Robot:
    
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.weapon = Weapon.set_weapon(self)
        #self.attackStrength = 0

    #def attack(self, Dinosaur):
        #attackStrength = 0
        #self.attackStrength += self.weapon.power

    