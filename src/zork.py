import items

def Play_Zork():
    loop = 4
    print ("-------------------------------------------------")
    print ("Welcome to Zork - The Unofficial Python Version.")
    return loop


def exit_function(exit_inp):
    if exit_inp.lower() ==  'dead':
        exit()


#CHANGED CODE: Added function for the first location/room
def location1(north_house_inp, itemList):
    if north_house_inp.lower() == ("go south"):
        loop = 4
        living_status = "Alive"
    elif north_house_inp.lower() == ("swim"):
        print ("-----------------------------------------------------")
        print("You don't have a change of clothes and hyou arent here on vacation.")
        living_status = "Alive"
        loop = 1
    elif north_house_inp.lower() == ("fish"):
        print ("---")
        print("You spend some time fishing but nothing seems to bite.")
        living_status = "Alive"
        loop = 1
    elif north_house_inp.lower() == ("kick the bucket"):
        print ("----------")
        print ("You die.")
        print ("----------------------")
        living_status = "Dead"
        dead_inp = living_status
        exit_function(dead_inp)
    else:
        print("---------------")
        loop = 1
        living_status = "Alive"
    return [loop, living_status]




#CHANGED CODE: Added function for the fourth location/room
def location4(second, itemList):
    if second.lower() == ("take mailbox"):
        print ("----------------------------------------------------")
        print("It is securely anchored.")
        living_status =  "Alive"
        loop = 4
    elif second.lower()== ('open mailbox'):
        print ("-----------------------------------------------------")
        print("Opening the small mailbox reveals a leaflet.")
        living_status = 'Alive'
        loop = 4
    elif second.lower()==("go north"):
        loop = 1
        living_status = "Alive"
    elif second.lower()==('open door'):
        print ("-----------------------------------------------------")
        print ("the door cannot be opened")
        living_status = 'Alive'
        loop = 4
    elif second.lower()==("take boards"):
        print ("-----------------------------------------------------")
        print("The boards are securely fastened.")
        living_status= 'Alive'
        loop = 4
    elif second.lower()==("look at house"):
        print("------------------------------------------------------")
        print ("the house is abeatufil olonia lhouse which is panted white. It...")
        living_status = 'Alive'
        loop = 4
    elif second.lower() == ("go southwest"):
        loop = 8
        living_status = 'Alive'
    elif second.lower()==("read leaflet"):
        print ("-----------------------------------------------------")
        print ("Welcome to the Unofficial Python Version of Zork. Your mission is to find a Jade Statue.")
        living_status = 'Alive'
        loop = 4
    elif second.lower()==("going east"):
        loop = 12
        living_status=("Alive")
    elif second.lower()==("kick the bucket"):
        print ("-----------------------------------------------------")
        print ("You die. ")
        print ("-----------------------------------------------------")
        living_status = "Dead"
        dead_inp = living_status
        exit_function(dead_inp)
    else:
        print ("-----------------------------------------------------")
        loop = 1
        living_status = "Alive"
    return [loop, living_status]







#CHANGED CODE: Added location for eigth location/room
def location8(forest_inp, itemList):
    if forest_inp.lower()== ("go west"):
        print("------------------------------------------------------")
        print("You would need a machete to further west.")
        living_status = "Alive"
        loop = 8
    elif forest_inp.lower()== ("go north"):
        print ('-----------------------------------------------------')
        print ("the forest beocmes impenetrable to the north.")
        living_status = "Alive"
        loop = 8
    elif forest_inp.lower()== ('go south'):
        print ("-----------------------------------------------------")
        print ("Storm-tossed trees block your way.")
        living_status = "Alive"
        loop = 8
    elif forest_inp.lower()== ("go east"):
        loop = 9
        living_status = "Alive"
    elif forest_inp.lower()== ("kick the bucket"):
        print ("-----------------------------------------------------")
        print ("you die.")
        print ("-----------------------------------------------------")
        living_status = "Dead"
        dead_inp = living_status
        exit_function(dead_inp)
    else:
        print ("-----------------------------------------------------")
        loop = 8
        living.status = 'Alive'
    return [loop, living_status]




#CHANGED CODE: Added function for ninth location/room
def location9(grating_inp, itemList):
    if grating_inp.lower() == ("go south"):
        print ("-----------------------------------------------------")
        print ("You see a large ogre and turn around.")
        living_status = "Alive"
        loop = 9
    elif grating_inp.lower() == ("descend grating"):
        loop = 10
        living_status = "Alive"
        dead_inp = living_status
        exit_function(dead_inp)
    else:
        print ("-----------------------------------------------------")
        loop = 9
        living_status = "Alive"
    return [loop, living_status]




#CHANGED CODE: Added function for tenth location/code
def location10(cave_inp, itemList):
    if cave_inp.lower() == ("descend staircase"):
        loop = 11
        living_status = "Alive"
    elif cave_inp.lower() == ("take skeleton"):
        print ("------------------------------------------------------")
        print ("Why would you do that? Are you some sort of sicko?")
        living_status = "Alive"
        loop = 10
    elif cave_inp.lower() == ("light up room"):
        print ("------------------------------------------------------")
        print ("I have two questions: Why and With What?")
        living_status = "Alive"
        loop = 10
    elif cave_inp.lower() == ('go down staircase'):
        loop = 11
        living_status = "Alive"
    elif cave_inp.lower() == ("scale staircase"):
        loop = 11
        living_status = "Alive"
    elif cave_inp.lower() == ("smash skeleton"):
        print ("------------------------------------------------------")
        print ("Sick person. Have some respect mate.")
        living_status = "Alive"
        loop = 10
    elif cave_inp.lower() == ("light up room"):
        print ("------------------------------------------------------")
        print ("you would need a torch to do that.")
        living_status = "Alive"
        loop = 10
    elif cave_inp.lower() == ("break skeleton"):
        print ("------------------------------------------------------")
        print ("I have two questions. Why and With What?")
        living_status = 'Alive'
        loop = 10
    elif cave_inp.lower() == ("go down staircase"):
        loop = 11
        living_status = "Alive"
    elif cave_inp.lower() == ("scale staircase"):
        loop = 11
        living_status = "Alive"
    elif cave_inp.lower() == ("kick the bucket"):
        print ("------------------------------------------------------")
        print ("you die")
        print ("------------------------------------------------------")
        living_status = 'Dead'
        dead_inp = living_status
        exit_function(dead_inp)
    elif cave_inp.lower() == ("scale staircase"):
        loop = 11
    else:
        print ("------------------------------------------------------")
        loop = 10
        living_status = 'Alive'
    return [loop, living_status]




#CHANGED CODE: Added function for eleventh location/room
def location11(last_inp, itemList):
    if last_inp.lower() == ("open trunk"):
        print ("------------------------------------------------------")
        print ("You have found the Jade Statue and have completed your guest!")
        print ("You win!")
        exit()
    elif last_inp.lower()== ("kick the bucket"):
        print ("------------------------------------------------------")
        print ("you die.")
        print ("------------------------------------------------------")
        living_status = "Dead"
        dead_inp = input("Do you want to continue? Y/N ")
    else:
        print ("------------------------------------------------------")
        loop = 11
        living_status = 'Alive'
    return [loop, living_status]
