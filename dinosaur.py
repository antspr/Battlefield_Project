from weapon import Weapon
class Dinosaur:
    def __init__(self, name, attack_power):
        self.name = name
        self.power = attack_power
        self.health = 100

    def attack(self,robot):
        robot = ''