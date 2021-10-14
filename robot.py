from weapon import Weapon
class Robot:
    
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.weapon = Weapon.set_weapon(self)

    def attack(self, dinosaur):
        dinosaur = ''
        
        

    