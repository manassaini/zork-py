import zork

def PrintOutput(s):
    print ("OUTPUT", s)

loop = zork.Play_Zork()

while True:
    while loop == 4:
        print ("-------------------------------------------------")
        print ("You are standing in an open field west of a white house, with a boarded front door")
        print ("You can see a small lake to the north.")
        print ("(A secret path leads southwest into the forest.)")
        print ("There is a small mailbox.")
        action = input("What do you do? ")
        room_status = zork.location4(action, [" "])
        loop = room_status[0]
    while loop == 1:
        print ("-------------------------------------------------")
        print ("You find yourself at the edge of a beautiful lake aside rolling hills.")
        print ("A small pier juts out into the lake.")
        print ("A fishing rod rests on the pier.")
        print ("(You can see a white house in the distance to the south.)")
        north_house_inp = input("What do you do? ")
        room_status = zork.location1(north_house_inp, [" "])
        loop = room_status[0]
    while loop == 8:
        print ("-------------------------------------------------")
        print ("You are in a clearing, with a forest surrounding you on all sides. A path leads south.")
        print ("There is an open grating, descending into darkness.")
        grating_inp = input("What do you do? ")
        room_status = zork.location9(grating_inp, [" "])
        loop = room_status[0]
    while loop == 10:
        print ("-------------------------------------------------")
        print ("You are in a tiny cave with a dark, forbidding staircase leading down.")
        print ("There is a skeleton of a human male in one corner.")
        cave_inp = input("What do you do? ")
        room_status = zork.location10(cave_inp, [" "])
        loop = room_status[0]
    while loop == 11:
        print ("-------------------------------------------------")
        print ("You have entered a mud-floored room.")
        print ("Lying half buried in the mud is an old trunk, bulging with jewels.")
        last_inp = input("What do you do? ")
        room_status = zork.location11(last_inp, [" "])
        loop = room_status[0]
    #while loop == 12:
