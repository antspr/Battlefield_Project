from robot import Robot

class Fleet:
    def __init__(self):
        self.robots = []

    def create_fleet(self):
        robots_00 = Robot('Antoine')
        robots_01 = Robot('Mike')
        robots_02 = Robot('Jimmy')
        self.robots.append(robots_00)
        self.robots.append(robots_01)
        self.robots.append(robots_02)
        return self.robots