import random

class Dragon:

    def __init__(self):

        self.identifier = "D"
        self.name = "Dragon"
        self.bag = []


    def move(self,nearby_creatures):

        return random.choice([9,10,11,12,13,14,15,16,9,10,11,12,13,14,15,16,9,10,11,12,13,14,15,16,
                1,2,3,4,5,6,7,8,17,18,19,20,21,22,23,24,1,2,3,4,5,6,7,8,17,18,19,20,21,22,23,24] + [i for i in range(25,49)])

    def attack(self,opp_id):

        if self.bag == []:
            self.bag = [1,2,3,4,5]
            random.shuffle(self.bag)

        return self.bag.pop()