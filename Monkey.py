import random

class Monkey:

    def __init__(self):

        self.identifier = "M"
        self.name = "Monkey"


    def move(self,nearby_creatures):

        return random.choice([25,26,28,29,31,32,34,35,37,38,40,41,43,44,46,47,49,50,51,52,49,50,51,52,49,50,51,52])

    def attack(self,opp_id):

        return random.choice([1,2,5])
