from dinosaur import Dinosaur
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
        return 'Welcome to Battlefield: Robots vs Dinos'

    def battle(self):
        robots = []
        dinos = []
        for robot in robots:
            robots += range(0,len(robots)-1)
        for dino in dinos:
            dinos += range(0,len(dinos))
        return robots, dinos

    def dino_turn(self, dinosaur):
        dino_turn = True
        while dino_turn == True :
            herd_index = 0
            for dinosaur in self.herd:
                herd_index += 1
                break
            return self.herd[herd_index]
        dino_turn == False
        
    def robot_turn(self, robot):
        robot_turn = True
        while robot_turn == True :
            fleet_index = 0
            for robot in self.herd:
                fleet_index += 1
                break
            return self.herd[fleet_index]
        robot_turn == False

    def show_dino_opponent_option(self):
        pass

    def show_robo_opponent_option(self):
        pass

    def display_winner(self):
        pass