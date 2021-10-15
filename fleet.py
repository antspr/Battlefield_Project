from robot import Robot

class Fleet:
    def __init__(self):
        self.fleet = []

    def create_fleet(self):
        robot_one = Robot('Antoine')
        robot_two = Robot('Mike')
        robot_three = Robot('Jimmy')
        
        self.fleet.append(robot_one)
        self.fleet.append(robot_two)
        self.fleet.append(robot_three)
       
        
        return self.fleet