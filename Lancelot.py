import random

class Lancelot:

   #OPTIONAL CODE GOES HERE

    def __init__(self):

        self.identifier = "K"
        #THIS ABSOLUTELY MAY NOT BE MODIFIED, UNDER PENALTY OF DEATH.

        self.name = "Lancelot"
        #THIS IS USED BY THE GUI, AND OTHER CREATURES CANNOT SEE IT. MAKE SURE IT IS UNIQUE TO YOUR KNIGHT.


    def move(self,nearby_creatures):

        #REQUIRED CODE HERE. MUST RETURN A NUMBER BETWEEN 0 and 8 INCLUSIVE

        return random.randint(0,8)

    def attack(self,opp_id):

        return random.randint(1,5)

        #REQUIRED CODE HERE. MUST RETURN A NUMBER BETWEEN 0 and 5 INCLUSIVE

    #MORE OPTIONAL CODE GOES HERE