import random

class Witch:

    def __init__(self):

        self.identifier = "W"
        self.name = "Witch"

    def move(self,nearby_creatures):

        return random.choice([1,2,3,4,5,6,7,8,17,18,19,20,21,22,23,24])

    def attack(self,opp_id):

        return random.choice([3,5])
