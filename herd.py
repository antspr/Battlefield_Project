from dinosaur import Dinosaur
class Herd:
    def __init__(self):
        self.dinosaurs = []

    def create_herd(self):
        dinosaur_one = Dinosaur('TRex', 25)
        dinosaur_two = Dinosaur('Triceratops', 5)
        dinosaur_three = Dinosaur('Velociraptor', 10)
        dino_herd =[dinosaur_one, dinosaur_two, dinosaur_three]
        dino_herd == self
        return self