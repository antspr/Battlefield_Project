from dinosaur import Dinosaur
from robot import Robot
from fleet import Fleet
from herd import Herd


class Battlefield :
    def __init__(self):
        self.fleet = Fleet()
        self.herd = Herd()

    def run_game(self):
        self.display_welcome()
        self.battle()


    def display_welcome(self):
        self.fleet = self.fleet.robots
        self.herd = self.herd.dinosaurs
        print('Welcome to Battlefield: Robots vs Dinosaurs')

    def battle(self):
        robot_attacker = 0
        dinosaur_attacker = 0
        for robots in self.fleet :
            robot_attacker += 1
        for dinosaurs in self.herd :
            dinosaur_attacker += 1    
        self.dino_turn()
        self.robot_turn()
#[range(0,len(self.herd)-1,1)]
#[range(0,len(self.fleet)-1,1)]
        # dinosaur = dinosaur
        # dinosaurs = [range(0,len(self.herd)-1)]
        # attack_dinosaur = 0
        # dino_turn = True    
        # dinosaur = self.herd[attack_dinosaur]    
        # while dino_turn == True :
        #     herd_index = 0
        #     for dinosaur in self.herd:
        #         herd_index += 1
        #     if herd_index == 3:
        #         attack_dinosaur == 0
        #         herd_index == attack_dinosaur
        #     else:
        #         attack_dinosaur += 1
        # dino_turn == False
    def dino_turn(self, dinosaur):
        dinosaur = dinosaur
        dinosaur_turn = True
        while dinosaur_turn == True:
            herd_index = 0
            for dinosaur in self.herd:
                herd_index += 1
                dinosaur_turn == False
            if herd_index == 3:
                herd_index == 0
            else:
                dinosaur_turn ==True
        return herd_index
        
    def robot_turn(self, robot):
        
        robot = robot
        robot_turn = True        
        while robot_turn == True :
            fleet_index = 0
            for robot in self.fleet:
                fleet_index += 1
        robot_turn == False

    def show_dino_opponent_option(self):
        dinosaurs = self.herd
        for dinosaur in dinosaurs:
            print(dinosaur.name, dinosaur.health)
        
    def show_robot_opponent_option(self):
        robots = self.fleet
        for robot in robots:
            print(robot.name, robot.health)

    def display_winner(self):
        if self.herd.dinosaur.health in self.herd == 0:
            self.herd.pop()
