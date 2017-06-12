import random

class Voidwalker:

    def __init__(self):

        self.identifier = "V"
        self.name = "Voidwalker"


    def move(self,nearby_creatures):

        movementdict = {
            10 : [2,3],
            12 : [3,2],
            13 : [3,4],
            15 : [4,3],
            17 : [1,1],
            19 : [1,5],
            21 : [5,5],
            23 : [5,1]
        }

        for possible_square in [10,12,13,15,17,19,21,23]:

            movement = movementdict[possible_square]

            if nearby_creatures[movement[0]][movement[1]] == "K":
                if random.randint(1,4) != 4:
                    return possible_square

        return random.choice([10,12,13,15,17,19,21,23])

    def attack(self,opp_id):


        #This really shouldn't ever happen, since voidwalkers kill all instantly, but if it does...
        return 0
