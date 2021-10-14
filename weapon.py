class Weapon:
    # name = input('Weapon name:  ')
    # attack_power = input('Weapon strength: ')
    def __init__(self, name, attack_power):
        self.name = name
        self.power = attack_power

    def set_weapon(self):
        name = input('Weapon name:  ')
        self.power = int(input('Weapon strength: '))
        return name, self.power
        

