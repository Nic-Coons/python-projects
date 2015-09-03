

def start():
    print ("Hello and welcome!")
    name = input("What is your name: ")
    print ('Welcome, '+name+'!')
    global quest
    quest = input("What is your quest: ")
    print (quest)
    color = input("What... is your favorite color: ")
    print ("The purpose of this game is to seek the Holy Grail!\n")
    print ("Whether you find it or not, and how you find it, is up to you\n \n")
    choice = input("Let's begin! You start in a field. Do you go east, or west?\n")
    if choice == "east":
        east()
    if choice == "west":
        west()
    else:
        print ("That is not a valid quest\n")
        start()

def east():
    print ("So you go east! You are searching for the sunrise when you encounter a goblin.\n")
    goblin = input("What do you do?\n")
    if goblin == "talk":
        goblinTalk()
    if goblin == "fight":
        goblinFight()
    if goblin == "ignore":
        ignore()
    else:
        print ("That is not a valid quest. You may talk, fight, or ignore the goblin \n")
        east()

def goblinTalk():
    print ("You talk to the goblin\n \n")
    print ("He says you smell funny")
    insult = input("Are you insulted? Y/N")
    if insult == "Y":
        print ("How dare that goblin insult you!\n")
        goblinFight()
    if insult == "N":
        print ("Well, you've got tough skin. Rubber and Glue, eh?\n \n")
        print ("Anyway, you ask him if he's seen the Holy Grail. He tells you that you're mixing your genres, but his best guess is to the north...\n \n \n \n")
        direction = input("do you go north or south?\n")
        if direction == "north":
            north()
        if direction == "south":
            south()
        else:
            print ("Not a valid direction, maybe you need to talk to the goblin again.\n")
            goblinTalk()

def goblinFight():
    print("Violence might be the answer!\n")
    attack = input("Do you attack with your sword, or punch him?\n")
    if attack == "sword":
        print("I don't remember giving you a sword!\n")
        goblinFight()
    if attack == "punch":
        print ("You punched the goblin!\n")
        print ("Goblin: OW! The hell human? What was that for?\n")
        print ("You demand infomation on the Holy Grail\n")
        print ("He tells you that you're mixing your genres, but his best guess is to the south\n")
        direction = input("do you go north or south?\n")
        if direction == "north":
            north()
        if direction == "south":
            south()
        else:
            print ("Not a valid direction, maybe you need to talk to the goblin again.\n")
            goblinTalk()


    
def ignore():
    print ("You don't want to talk to the nasty goblin and continue on.\n")
    print ("You can either go north or south from here\n")
    direction = input("do you go north or south?\n")
    if direction == "north":
        north()
    if direction == "south":
        south()
    else:
        print ("Not a valid direction.")
        ignore()

def north():
    if quest == "To seek the holy grail":
        print("You found the Holy Grail! Awesome! GAME OVER\n \n")
        start()
    else:
        print ("You wander north for many miles, and unbeknownst to you pass the Holy Grail. I guess your quest wasn't very focused\n\n\n")
        start()
def south():
    print("Oh darn, you died. GAME OVER\n \n")
    start()

def west():
    print("You go west! You follow the arc of the sun for many miles until you come across a cave")
    enter = input("Do you enter the cave? Y/N \n")
    if enter == "Y":
        print ("Someone isn't genre savy. The rabbit kills you")
        print ("GAME OVER\n \n \n \n \n")
        start()
    else:
        print("Eh, you don't want to go there. Looks like theres a dangerous rabbit there anyway.\n")
        print("From here, you can go north or south")
        direction = input("do you go north or south?\n")
        if direction == "north":
            north()
        if direction == "south":
            south()
        else:
            print ("Not a valid direction.")
            direction = input("do you go north or south?\n")
            if direction == "north":
                north()
            if direction == "south":
                south()
            else:
                print ("Not a valid direction. Now you're stuck, smartass")
    
start()
