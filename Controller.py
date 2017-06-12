import importlib
import math
import random
import pygame
import colorsys
pygame.init()

def spawn_python_creature(creature):

    #Baz's Note: I stole this off stackoverflow and changed it a bit. I have no clue how it works.

    # load the module, will raise ImportError if module cannot be loaded
    m = importlib.import_module(creature)
    # get the class, will raise AttributeError if class cannot be found
    c = getattr(m, creature)
    return c()

def hsv2rgb(h,s,v):
    colors = list(colorsys.hsv_to_rgb(h,s,v))
    colors[0] = int(255 * colors[0])
    colors[1] = int(255 * colors[1])
    colors[2] = int(255 * colors[2])
    return (colors[0],colors[1],colors[2])

def generate_colors(amount):
    color_list = []
    return [hsv2rgb(((i/amount)), 0.5065, 0.602) for i in range(amount)]

    for i in range(amount):

        hue = (360 * (i/amount))

        color_list.append(hsv2rgb(hue, 0.5065, 0.602))

    return color_list

def sort_key(list):
    return (-list[1],-list[2],-list[4])

def sort_key2(list):
    return (-list[5],-list[7],-list[6])

def draw():

    screen.fill((204,204,204))

    y_coordinate = 25

    battletxt = largefont.render("Battle #" + str(battlenum), True, (0,0,0))

    screen.blit(font.render("Turn: " + str(turn), True, (0,0,0)),(25,525 + battletxt.get_height() + 5))

    screen.blit(font.render("Press B to start a Bettle. Press P to Print the entire scoreboard to console.",True,(0,0,0)),(25,725))

    screen.blit(battletxt,(25,525))

    log = largefont.render("Combat Log",True,(0,0,0))

    scoretxt = largefont.render("Scoreboard",True,(0,0,0))

    screen.blit(scoretxt,(555,525))

    screen.blit(log,(200,525))
    for i in range(10):
        screen.blit(font.render(combat_log[i], True, (0,0,0)),(200,(log.get_height() + 525)+15*(i)))

    for row in forest:
        x_coordinate = 25
        for creature in row:
            if creature == "":
                pass
            else:
                color_ind = creatures.index(creature.name)


                pygame.draw.rect(screen, color_list[creatures.index(creature.name)], (x_coordinate, y_coordinate, gridsize, gridsize))


            x_coordinate += gridsize

        y_coordinate += gridsize

    pygame.draw.rect(screen, (0, 0, 0),
                     (25,25,gridsize * forest_size,gridsize * forest_size),1)

    y_coordinate = 25

    creature_stat = [[creatures[i],creature_counts[i],died_at[i],color_list[i],kills[i],
                      score[i],total_kills[i],survivors[i]] for i in range(len(creatures))]

    creature_stat = sorted(creature_stat, key=sort_key)

    for i in creature_stat:

        if i[2] == -1:
            text = font.render(i[0] + ": " + str(i[1]) + " (" + str(i[4]) + " Kills)",True,i[3])
        else:
            text = font.render(i[0] + ": " + str(i[1]) + " (Eliminated Turn " + str(i[2]) + ")" + " (" + str(i[4]) + " Kills)",True,(0,0,0))
        screen.blit(text,(525,y_coordinate))
        y_coordinate += 15

    creature_stat = sorted(creature_stat,key=sort_key2)

    creature_stat = [i for i in creature_stat if i[0] != "Voidwalker"]

    if in_battle:
        for i in creature_stat:
            i[6] += i[4]
            i[7] += i[1]

    y_coordinate = 525

    for i in range(min(len(creatures)-1,10)):

        j = creature_stat[i]

        string = "#" + str(i+1) + ": " + j[0] + " - " + str(j[5]) + " Points" + " (" + str(j[7]) + " Total Survivors)" + " (" + str(j[6]) + " Total Kills)"

        screen.blit(font.render(string,True,j[3]),(555,(scoretxt.get_height() + 525) + (15 * i)))

        y_coordinate += 15

def rpsls_win(p1,p2):

    if p1 == 0 and p2 != 0:
        return 2 #P1 killed themself
    elif p1 == 0 and p2 == 0:
        return 3 #They Both Killed Themselves
    elif p1 != 0 and p2 == 0:
        return 1 #P2 Killed themself
    elif p1 == p2:
        return 0 #Draw
    else:

        player1_win_conditions = [
            "X", #SUI
            [4,3], #ROCK
            [1,5], #PAPER
            [2,4], #SCISSORS
            [5,2], #LIZARD
            [3,1], #SPOCK/DEMON
        ]

        if p2 in player1_win_conditions[p1]:
            return 1
        else:
            return 2

def update_creature_count():

    counts = [0 for i in creature_counts]

    for row in forest:
        for creature in row:
            if creature == "":
                pass
            else:
                counts[creatures.index(creature.name)] += 1

    return counts

#MAKE IMPORTANT VARIABLES

font = pygame.font.SysFont("Trebuchet MS",16)
largefont = pygame.font.SysFont("Trebuchet MS",36)
screen = pygame.display.set_mode((1000, 760))

movement_list = [
   #[Y,X],
    [0,0],
    [-2,-1],
    [-2,1],
    [-1,2],
    [1,2],
    [2,1],
    [2,-1],
    [1,-2],
    [-1,-2],
    [-1,-1],
    [-1,0],
    [-1,1],
    [0,-1],
    [0,1],
    [1,-1],
    [1,0],
    [1,1],
    [-2,-2],
    [-2,0],
    [-2,2],
    [0,2],
    [2,2],
    [2,0],
    [2,-2],
    [0,-2],
    [-3,-2],
    [-3,-1],
    [-3,0],
    [-3,1],
    [-3,2],
    [-3,3],
    [-2,3],
    [-1,3],
    [0,3],
    [1,3],
    [2,3],
    [3,3],
    [3,2],
    [3,1],
    [3,0],
    [3,-1],
    [3,-2],
    [3,-3],
    [2,-3],
    [1,-3],
    [0,-3],
    [-1,-3],
    [-2,-3],
    [-3,-3],
    [-4,0],
    [0,4],
    [4,0],
    [0,-4],
]

creatures = [
    "Elf",
    "Rock",
    "Witch",
    "Monkey",
    "Dragon",
    "Voidwalker",
    "Lancelot",
]

color_list = generate_colors(len(creatures))

score = [0 for i in creatures]
total_kills  = [0 for i in creatures]
survivors = [0 for i in creatures]
battlenum = 1
in_battle = 1

#INITIALIZE PLAYING FIELD

combat_log = ["" for i in range(10)]

creature_counts = [0 for i in creatures]

died_at = [-1 for i in creatures]

kills = [0 for i in creatures]

forest_size = int(math.sqrt(len(creatures))*20)

gridsize = 500//forest_size

forest = [["" for i in range(forest_size)] for j in range(forest_size)]

for name in creatures:

    if name == "Voidwalker":
        spawncount = (forest_size**2)//1000
    else:
        spawncount = 100

    for i in range(spawncount):

        x = random.randint(0,forest_size-1)
        y = random.randint(0,forest_size-1)

        while forest[x][y] != "":
            x = random.randint(0, forest_size - 1)
            y = random.randint(0, forest_size - 1)

        forest[x][y] = spawn_python_creature(name)

turn = 0



while True:

    event = pygame.event.poll()

    if event.type == pygame.QUIT:
        exit()

    if event.type == pygame.KEYDOWN:
        key = event.key

        if key == pygame.K_p:

            creature_stat = [[creatures[i], creature_counts[i], died_at[i], color_list[i], kills[i],
                              score[i], total_kills[i], survivors[i]] for i in range(len(creatures))]

            creature_stat = sorted(creature_stat, key=sort_key2)

            creature_stat = [i for i in creature_stat if i[0] != "Voidwalker"]

            y_coordinate = 525

            for i in range(min(len(creatures) - 1, 10)):
                j = creature_stat[i]

                string = "#" + str(i + 1) + ": " + j[0] + " - " + str(j[5]) + " Points" + " (" + str(
                    j[7]) + " Total Survivors)" + " (" + str(j[6]) + " Total Kills)"

                print(string)

        if key == pygame.K_b:

            combat_log = ["" for i in range(10)]

            creature_counts = [0 for i in creatures]

            died_at = [-1 for i in creatures]

            kills = [0 for i in creatures]

            forest_size = int(math.sqrt(len(creatures)) * 20)

            gridsize = 500 // forest_size

            forest = [["" for i in range(forest_size)] for j in range(forest_size)]

            for name in creatures:

                if name == "Voidwalker":
                    spawncount = (forest_size ** 2) // 1000
                else:
                    spawncount = 100

                for i in range(spawncount):

                    x = random.randint(0, forest_size - 1)
                    y = random.randint(0, forest_size - 1)

                    while forest[x][y] != "":
                        x = random.randint(0, forest_size - 1)
                        y = random.randint(0, forest_size - 1)

                    forest[x][y] = spawn_python_creature(name)

            turn = 0
            battlenum += 1
            in_battle += 1


    while turn < 1000: #i know a for loop is better but i'm using turn in draw() so shut up
        events = pygame.event.poll()

        if events.type == pygame.QUIT:
            exit()


        creature_counts = update_creature_count()

        for i in range(len(creatures)):
            if creature_counts[i] == 0 and died_at[i] == -1:
                died_at[i] = turn

        turn += 1

        #DO MOVEMENTS

        new_forest = [[[] for i in range(forest_size)] for j in range(forest_size)]

        for row in range(forest_size):
            for col in range(forest_size):

                creature = forest[row][col]

                if creature == "":
                    pass
                else:

                    #generate surroundings

                    surroundings = [["" for i in range(7)] for j in range(7)]

                    row_list = [row-3,row-2,row-1,row,row+1,row+2,row+3]
                    col_list = [col-3,col-2,col-1,col,col+1,col+2,col+3]

                    row_list = [i % forest_size for i in row_list]
                    col_list = [i % forest_size for i in col_list]




                    for surr_row in row_list:
                        for surr_col in col_list:
                            if forest[surr_row][surr_col] != "":

                                row_ind = row_list.index(surr_row)
                                col_ind = col_list.index(surr_col)


                                surroundings[row_ind][col_ind] = forest[surr_row][surr_col].identifier


                    try:
                        movement_result = creature.move(surroundings)

                        if creature.identifier == "K":
                            assert movement_result in [0,1,2,3,4,5,6,7,8]

                        movement_result = movement_list[movement_result]

                    except Exception as ex:
                        print(type(ex).__name__, "Exception thrown by", creature, "during movement. Position", row, col, ex.args)
                        movement_result = [0,0]

                    new_row = (row + movement_result[0]) % forest_size
                    new_col = (col + movement_result[1]) % forest_size

                    if creature.name in ["Elf","Witch","Monkey","Dragon","Voidwalker","Rock"] or creature.identifier == "K":
                        new_forest[new_row][new_col].append(creature)

        forest = [["" for i in range(forest_size)] for j in range(forest_size)]

        for row in range(forest_size):
            for col in range(forest_size):
                if len(new_forest[row][col]) == 0:
                    forest[row][col] = ""
                else:
                    length = len(new_forest[row][col])
                    while length != 1:

                        random.shuffle(new_forest[row][col])

                        if len(new_forest[row][col]) == 1:
                            break


                        p1i = 0
                        p2i = 1

                        p1c = new_forest[row][col][p1i]
                        p2c = new_forest[row][col][p2i]

                        if p1c.identifier != "V" and p2c.identifier != "V":

                            try:
                                p1f = p1c.attack(p2c.identifier)

                                if p1c.identifier == "K":
                                    assert p1f in [1,2,3,4,5]
                            except Exception as ex:
                                print(type(ex).__name__, "Exception thrown by", p1c, "during combat. Position",
                                      row, col, ex.args)
                                p1f = 0

                            try:
                                p2f = p2c.attack(p1c.identifier)

                                if p2c.identifier == "K":
                                    assert p2f in [1, 2, 3, 4, 5]
                            except Exception as ex:
                                print(type(ex).__name__, "Exception thrown by", p2c, "during combat. Position",
                                      row, col, ex.args)
                                p2f = 0

                            result = rpsls_win(p1f,p2f)




                            if result in [1,3]: #P1 wins OR double suicide
                                del new_forest[row][col][p2i]

                                if result != 3:
                                    combat_log.append("A " + p1c.name + " just defeated a " + p2c.name + " in Combat!")
                                    del combat_log[0]
                                    kills[creatures.index(p1c.name)] += 1

                            if result in [2,3]: #P2 wins OR double suicide
                                del new_forest[row][col][p1i]

                                if result != 3:
                                    del combat_log[0]
                                    combat_log.append("A " + p2c.name + " just defeated a " + p1c.name + " in Combat!")
                                    kills[creatures.index(p2c.name)] += 1
                            #on draw, nothing happens


                        else:
                            if p2c.identifier != "V":

                                combat_log.append("A Voidwalker just consumed a " + p2c.name + ".")

                                new_forest[row][col] = [x for x in new_forest[row][col] if x != p2c]

                                kills[creatures.index("Voidwalker")] += 1
                            else:

                                combat_log.append("A Voidwalker just consumed a " + p1c.name + ".")

                                new_forest[row][col] = [x for x in new_forest[row][col] if x != p1c]

                                kills[creatures.index("Voidwalker")] += 1

                        length = len(new_forest[row][col])

                    forest[row][col] = new_forest[row][col][0]

        pygame.time.wait(50)
        draw()
        pygame.display.flip()


    if in_battle:

        #handle score
        creature_ind = 0

        creature_stat = [[creatures[i], creature_counts[i], died_at[i], color_list[i], kills[i]] for i in
                         range(len(creatures))]
        creature_stat = sorted(creature_stat,key=sort_key)


        for creature in creature_stat:

            survivors[creatures.index(creature[0])] += creature[1]
            total_kills[creatures.index(creature[0])] += creature[4]

            if creature[0] == "Voidwalker":
                pass
            else:
                score[creatures.index(creature[0])] += int(100 * (0.8**(creature_ind)))
                creature_ind += 1

        in_battle = 0

    draw()
    pygame.display.flip()
