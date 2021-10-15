from weapon import Weapon
class Robot:
    
    def __init__(self, name):
        self.name = name
        self.health = int
        self.weapon = []

    def attack(self, dinosaur):
        self.weapon = Weapon.set_weapon(self)
        
        

    