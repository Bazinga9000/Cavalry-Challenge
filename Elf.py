import random

class Elf:

    def __init__(self):

        self.identifier = "E"
        self.name = "Elf"


    def move(self,nearby_creatures):

        return random.randint(9,16)

    def attack(self,opp_id):

        return random.choice([1,2,4])
