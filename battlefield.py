from fleet import Fleet
from herd import Herd


class Battlefield :
    def __init__(self):
        self.fleet = Fleet()
        self.herd = Herd()

    def run_game(self):
        self.fleet = Fleet.create_fleet(self)
        self.herd = Herd.create_herd(self)

    def display_welcome(self):
        print('Welcome to Battlefield: Robots vs Dinos')

    def battle(self):
        pass

    def dino_turn(self, dinosaur):
        pass

    def robot_turn(self, robot):
        pass

    def show_dino_opponent_option(self):
        pass

    def show_robo_opponent_option(self):
        pass

    def display_winner(self):
        pass