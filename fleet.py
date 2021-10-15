from robot import Robot

class Fleet:
    def __init__(self):
        self.fleet = []

    def create_fleet(self):
        robot_one = Robot('Antoine')
        robot_two = Robot('Mike')
        robot_three = Robot('Jimmy')
        robot_fleet = [robot_one,robot_two,robot_three]
        robot_fleet == self
       
        return self