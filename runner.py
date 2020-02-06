import rooms
from textwrap import dedent


class Runner(object):
    rooms = {
        'room1' : rooms.Room1(),
        'room2' : rooms.Room2(),
        'room3' : rooms.Room3(),
        'room4' : rooms.Room4(),
        'room5' : rooms.Room5(),
        'room6' : rooms.Room6(),
        'Death' : rooms.Death()
    }

    def random_room(self, room_name):
        #Is used by current room to see which room the player currently is in,
        #by finding each name over and over
        return Runner.rooms.get(room_name)
    def play(self):
        print(dedent("""You are the son of the dead leader of the greatest army in
        the universe, and must go through random rooms generated through reality
        to find the four parts of the staff of power in order to fix reality
        and bring back the GAA. Along the way, you will face dangerous enemies,
        who require you to be smart or use the pieces correctly You start
        with nothing and must escape while facing enemies and collecting the
        weapons"""))
        current_room = Runner.random_room(self, 'room1')
        #Starts with the opening room no matter what, as set in the above code
        last_room = Runner.random_room(self, 'room6')
        #states which scene is the ending
        while current_room != last_room:
            #Once the start room moves, it becomes room2, and room2 becomes the current room
            next_room = current_room.enter()
            #repeats as each room becomes a new room, and checks that it is not the end room
            current_room = Runner.random_room(self, next_room)
            #Sets the current room as whatever the current room is, so the cycle can repeat for each room
        current_room.enter()
