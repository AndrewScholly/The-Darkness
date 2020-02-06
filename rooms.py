import test_value
import random_functions
from textwrap import dedent
class Room(object):
    def enter(self):
        print("I have a plan")
        exit(1)

#Currently, I have been unable to find a way to properly use a function with
#the y variable, despite the fact they are repeated multiple times and
#are quite messy with the code, same with the check for all of the parts being
#collected



class Room1(Room):
    def enter(self):
        x = random_functions.random_number()
        #used for the randomization, for whether or not s piece is collected
        print(dedent("""You enter the corridor, looking around for the map to
the pieces, when a darkness being jumps out at you! Without any pieces yet, you
need to defeat the being somehow without touching him. There are a few rocks, a
scroll, and a mysterious blaster with warning signs on it nearby"""))
        fight = input(" ")
        #The following code is used for whatever the user puts in to decide the output
        if fight == "fire blaster":
            print("You destroyed the enemy, and moved on")
            if x == 1:
                #uses the x as a variable so there is a chance of collecting or not collecting stuff
                print("You find the map to the pieces and get the heck out of there")
                test_value.a = 1
                #get around the problem of vsriables defined in this room from reverting back to 0
                #if defined here in the eiter area
                y = random_functions.random_rooms()
                #a different random function, so it is not confuse
                if y == 2:
                    return 'room2'
                elif y == 3:
                    return 'room3'
                elif y == 4:
                    return 'room4'
                elif y == 5:
                    return 'room5'
            else:
                print("You don't manage to find the map, so you keep searching.")
                return 'room1'
        elif fight == "throw rock":
            print("The rock hits the being and does nothing")
            print("You died")
            return 'Death'
        elif fight == "throw scroll":
            print("The scroll does nothing")
            print("You died")
            return 'Death'
        else:
            #In case if the user puts something in wrong
            print("That is not a valid response. Try throwing or firing something")
            return 'room1'

class Room2(Room):
    def enter(self):
        if test_value.b == 1 and test_value.c == 1 and test_value.d == 1 and test_value.e == 1:
            return 'room6'
        elif test_value.b == 1:
            return 'room3'
        else:
            x = random_functions.random_number()
            print("You enter the room, a tall ceiling above you, looking around for the wand, when a fiery darkness demon jumps out at you!")
            if x == 1:
                test_value.b = 1
                print("You collect the wand")
                y = random_functions.random_rooms()
                if y == 2:
                    return 'room2'
                elif y == 3:
                    return 'room3'
                elif y == 4:
                    return 'room4'
                elif y == 5:
                    return 'room5'
            else:
                print("You don't manage to find the wand, so you keep searching.")
                y = random_functions.random_rooms()
                if y == 2:
                    return 'room2'
                elif y == 3:
                    return 'room3'
                elif y == 4:
                    return 'room4'
                elif y == 5:
                    return 'room5'


class Room3(Room):
    def enter(self):
        if test_value.b == 1 and test_value.c == 1 and test_value.d == 1 and test_value.e == 1:
            return 'room6'
        elif test_value.c == 1:
            return 'room4'
        else:
            x = random_functions.random_number()
            print("You enter the underground sewer, looking for the blaster")
            if x == 1:
                print("You collect the wand")
                test_value.c = 1
                y = random_functions.random_rooms()
                if y == 2:
                    return 'room2'
                elif y == 3:
                    return 'room3'
                elif y == 4:
                    return 'room4'
                elif y == 5:
                    return 'room5'
            else:
                print("You look everywhere and get tired, finding nothing")
                y = random_functions.random_rooms()
                if y == 2:
                    return 'room2'
                elif y == 3:
                    return 'room3'
                elif y == 4:
                    return 'room4'
                elif y == 5:
                    return 'room5'

class Room4(Room):
    def enter(self):
        if test_value.b == 1 and test_value.c == 1 and test_value.d == 1 and test_value.e == 1:
            return 'room6'
        elif test_value.d == 1:
            return 'room5'
        else:
            x = random_functions.random_number()
            print("You enter the apiary, what was once a glass ceiling has become a dark cover over you.")
            print("The sword must be here...")
            if x == 1:
                test_value.d = 1
                print("You collect the sword")
                y = random_functions.random_rooms()
                if y == 2:
                    return 'room2'
                elif y == 3:
                    return 'room3'
                elif y == 4:
                    return 'room4'
                elif y == 5:
                    return 'room5'
            else:
                print("Such bad luck, no sword!")
                y = random_functions.random_rooms()
                if y == 2:
                    return 'room2'
                elif y == 3:
                    return 'room3'
                elif y == 4:
                    return 'room4'
                elif y == 5:
                    return 'room5'

class Room5(Room):
    def enter(self):
        if test_value.b == 1 and test_value.c == 1 and test_value.d == 1 and test_value.e == 1:
            return 'room6'
        elif test_value.e == 1:
            return 'room2'
        else:
            x = random_functions.random_number()
            print("You enter the old temple, seemingly built in to this place, to find the saber")
            if x == 1:
                test_value.e = 1
                print("You collect the saber")
                y = random_functions.random_rooms()
                if y == 2:
                    return 'room2'
                elif y == 3:
                    return 'room3'
                elif y == 4:
                    return 'room4'
                elif y == 5:
                    return 'room5'
            else:
                print("You couldn't manage to find it, so you keep searching")
                y = random_functions.random_rooms()
                if y == 2:
                    return 'room2'
                elif y == 3:
                    return 'room3'
                elif y == 4:
                    return 'room4'
                elif y == 5:
                    return 'room5'

class Room6(Room):
    def enter(self):
        print("You enter the throne room, seeing the being of darkness up ahead")
        print("""You manage to reduce your enemy to the scraps of armour they were in.
                 You give your power to contain the armour and keep your enemy from reforming. You win!""")
class Death(Room):
    def enter(self):
        print("You died")
