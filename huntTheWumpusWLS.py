# ***************************************************************
# PROJECT: HuntTheWumpus
#
# FILE:	   huntTheWumpus.py
#
# EXEECUTION ENVIRONMENTS:
# Python 2.7 on Manjaro Linux 16
# Python 2.7 on Windows 10
#
# AUTHOR(S): Logan Warner
#
# ATTRIBUTION:
# From code by Michael P. Conlon
# micahel.conlon@sru.con
#
# Note:
# Copyright, 2001-2010, Michael P. Conlon.
# This program may be used by anyone, for any purpose whatsoever,
# provided that this copyright notice and attribution to author(s)
# remain. Licensing of derivative works must be under
# equivalent terms.
#
# DESCRIPTION
# A version of the classical "Hunt The Wumpus" game in Python 2.7
# ***************************************************************

# --------------
# Python imports
# --------------
import random
import re
from Player import Player
from Arrow import Arrow

# ---------
# Functions
# ---------


def give_instructions():
    print("")
    print('The Wumpus lives in a cave of 20 rooms.')
    print('Each room has 3 tunnels that lead to other rooms.')
    print('The Wumpus occasionally ventures out')
    print('to eat pets and children in a nearly village.')
    print('Since you are a renowned hunter you have been')
    print('commissioned to hunt and slay the Wumpus!')
    print('')
    print('Hazards!')
    print('---------')
    print('Two of the rooms have bottomless pits in them.')
    print('If you go into one of these rooms you will fall into')
    print('the pit and never be seen again! But there is a clue:')
    print('When you are in a room that has a tunnel that connects')
    print('to a room with a bottomless pit you will feel a draft.')
    print(' ')
    print('The Wumpus shares his cave with two giant bats.')
    print('These giant bats live in two different rooms. If you')
    print('enter one of these rooms, a giant bat will')
    print('grab you and take you to some other room at random.')
    print('This can possibly cost you your life!')
    print('If a giant bat takes you to another room, the bat')
    print('will take up abode in another random room.')
    print('When you are in a room that has a tunnel that connects')
    print('to a room with bats in it you will hear them.')
    print(' ')
    print('The WUMPUS')
    print('-----------')
    print('The Wumpus is not bothered by hazards.')
    print('He has sucker feet that can grip')
    print('the sides of the bottomless pits, and he is')
    print('too big for a bat to lift. Usually, he is asleep.')
    print('Two things wake him up: (1) you shooting an arrow,')
    print('or (2) you entering his room. If he wakes he either')
    print('moves to an adjacent room with probability 0.75')
    print('or stays where he is. If he ends up where you are,')
    print('he eats you; and the game is over.')
    print('When you are in a room that has a tunnel that connects')
    print('to a room with him in it you will smell him.')
    print(' ')
    print('YOU')
    print('---')
    print('The game starts with you (and five magic arrows) in an')
    print('empty room (no Wumpus, bats, or pits). ')
    print('You have three choices:')
    print('    s - shoot')
    print('    m - move')
    print('    q - quit')
    print('You can use one of the tunnels from the room you')
    print('are in and move to an adjacent room, OR')
    print('you can shoot a magic arrow. To shoot an arrow you tell')
    print('the computer which rooms (up to 5) the arrow is to')
    print('travel through. If a room, you listed is not a possible')
    print('path for the arrow from the current room - ')
    print('there is not a tunnel to the room you listed next)')
    print("the program selects a tunnel at random from the arrow's")
    print('current position(room) and continues to do so for as')
    print('many rooms as you listed. If your arrow hits the Wumpus')
    print('you win and collect your handsome commission.')
    print('If the arrow hits you, you die, and stay dead!\n')
#give_instructions()


class WumpusCave:
    def __init__(self):
        """
        Set up the initial cave contents and states
        """
        '''
        Algorthim
        ---------
        A01 Instantiate player
        A02 Initialize player
        A03 Initialize list room_paths and room_items
        A04 Initialize player_position
        '''
        self.player = Player()                                         #L01 L02
        self.room_paths, self.room_items = WumpusCave.make_room_layout()   #L03
        self.player_position = self.find_empty_room()                      #L04
    #__init__

    @staticmethod
    def reposition_randomly(roomNumPR):
        """Get a new, random, valid position number from an existing one"""
        '''
        Algorithm
        ---------
        A01 Seed the random number generator
        A02 Return input plus a random int [1, 19], rolling over at 20
        '''
        random.seed()                                                      #L01
        return (roomNumPR + random.randint(1, 19)) % 20                    #L02
    #reposition_randomly

    @staticmethod
    def make_room_layout():
        """
        Build a representation of the rooms for the game rooms
        and place non-player objects
        :rtype: object
        """
        '''
        Algorithm
        ---------
        A01 Initialize available paths
        A02 Set room_paths to sets representing paths to available vertices
            (indices) at each vertex (index)
        A03 Initialize room items
        A04 Seed random number generator
        A05 Append a bat to a random room,
            and another bat a random distance away
        A06 Append a pit to a random room,
            and another pit a random distance away
        A07 Append a Wumpus to a random room
        A08 Return available paths and room items
        '''
        room_paths = [None] * 20                                           #L01
        room_paths[0] = {1, 4, 7}                                          #L02
        room_paths[1] = {0, 2, 9}
        room_paths[2] = {1, 3, 11}
        room_paths[3] = {2, 4, 13}
        room_paths[4] = {0, 3, 5}
        room_paths[5] = {4, 6, 14}
        room_paths[6] = {5, 7, 16}
        room_paths[7] = {0, 6, 8}
        room_paths[8] = {7, 9, 17}
        room_paths[9] = {1, 8, 10}
        room_paths[10] = {9, 11, 18}
        room_paths[11] = {2, 10, 12}
        room_paths[12] = {11, 13, 19}
        room_paths[13] = {3, 12, 14}
        room_paths[14] = {5, 13, 15}
        room_paths[15] = {14, 16, 19}
        room_paths[16] = {6, 15, 17}
        room_paths[17] = {8, 16, 18}
        room_paths[18] = {10, 17, 19}
        room_paths[19] = {12, 15, 18}

        room_items = [set() for _ in range(20)]                            #L03
        random.seed()                                                      #L04
        bat_location = random.randint(0, 19)                               #L05
        room_items[bat_location].add('bat')
        room_items[WumpusCave.reposition_randomly(bat_location)].add('bat')
        pit_location = random.randint(0, 19)                               #L06
        room_items[pit_location].add('pit')
        room_items[WumpusCave.reposition_randomly(pit_location)].add('pit')
        wumpus_location = random.randint(0, 19)                            #L07
        room_items[wumpus_location].add('Wumpus')
        return room_paths, room_items                                      #L08
    #makeRoomLayout

    def find_empty_room(self):
        """
        Find the first room with no bats, pits, or Wumpus in it
        :rtype: int
        :return: first empty index in self.room_items
        """
        '''
        Algorithm
        ---------
        A01 Return first empty index in room_items
        '''
        for index, items in enumerate(self.room_items):                    #L01
            if not items:
                return index
    #find_empty_room

    def describe_nearby_room_effects(self):
        """
        Prints messages to describe what is in nearby rooms
        """
        '''
        Algorithm
        ---------
        A01 For rooms in available paths
            A02 If bat in the room
                A03 Display bat nearby message
            A04 If Wumpus in the room
                A05 Display Wumpus nearby message
            A06 If pit in the room
                A07 Display pit nearby message
        '''
        for room_number in self.room_paths[self.player_position]:          #L01
            if 'bat' in self.room_items[room_number]:                      #L02
                print("You hear bats nearby!")                             #L03
            if 'Wumpus' in self.room_items[room_number]:                   #L04
                print("It smells bad here!")                               #L05
            if 'pit' in self.room_items[room_number]:                      #L06
                print("It's drafty here!")                                 #L07
    #describe_nearby_room_effects

    def wake_wumpus(self):
        """
        Wakes the Wumpus from an arrow being fired
        """
        '''
        Algorithm
        ---------
        A01 Seed the random number generator
        A02 Display Wumpus waking message
        A03 If 75% chance
            A04 Display Wumpus moving message
            A05 Walk room list to find the Wumpus
                A06 If Wumpus in room
                    A07 Delete the Wumpus from items list
                    A08 Append a Wumpus to a new different random position
            A09 If player in room Wumpus entered
                A10 Call player.kill() with Wumpus death message
        '''
        random.seed()                                                      #L01
        print("The Wumpus hears the arrow and wakes up!")                  #L02
        if random.randint(0, 3) > 0:                                       #L03
            print("The Wumpus storms into another room...")                #L04
            for roomNum, room in enumerate(self.room_items):               #L05
                print(room)
                if 'Wumpus' in room:                                       #L06
                    room.remove('Wumpus')                                  #L07
                    new_wumpus_location =\
                        WumpusCave.reposition_randomly(roomNum)            #L08
                    self.room_items[new_wumpus_location] =\
                        self.room_items[new_wumpus_location].add('Wumpus')
            if 'Wumpus' in self.room_items[self.player_position]:          #L09
                self.player.kill("The Wumpus growls and eats you!")        #L10
    #wake_wumpus

    def shoot(self):
        """
        Method for dealing with the user opting to shoot an arrow
        """
        '''
        Algorithm
        ---------
        A01 If player has no arrows left
            A02 Display out of arrows message
            A03 Return
        A04 Obtain arrow path list
        A05 Parse arrow path list by splitting on a comma or space
                  with spaces leading and trailing
        A06 Walk (list comprehension) room_list
            A07 Convert to int
        A08 Append invalid room numbers to pad end of room list
        A09 Initialize arrow
        A10 Call wake_wumpus()
        A11 If player is dead
            A12 return
        A13 Walk room_list with nextRoomNum
            A14 Set nextRoomNum to valid room option
            A15 If Wumpus is in the room
                A16 Call player.kill with win message
                A17 Break
            A18 Else if player is in the room
                A19 Call player.kill with arrow death message
                A20 Break
            A21 Else
                A22 Display arrow no-hit message
        A23 Call player.loseArrow()
        '''
        if not self.player.hasArrows():                                    #L01
            print("You are out of arrows!")                                #L02
            return                                                         #L03
        room_list = re.compile('[ ]*[, ]?[ ]*').\
                    split(raw_input("Arrow path?> "))                 #L04 #L05
        room_list = [int(room_str) for room_str in room_list][:5]     #L06 #L07
        for index in range(5 - len(room_list)):                            #L08
            room_list.append(-1)

        arrow = Arrow(self.player_position, self.room_paths)               #L09
        self.wake_wumpus()                                                 #L10
        if not self.player.isAlive:                                        #L11
            return                                                         #L12
        for nextRoomNum in room_list:                                      #L13
            nextRoomNum = arrow.advance(nextRoomNum)                       #L14
            if 'Wumpus' in self.room_items[nextRoomNum]:                   #L15
                self.player.kill("You have slain the Wumpus! You win!")    #L16
                break                                                      #L17
            elif self.player_position == nextRoomNum:                      #L18
                self.player.kill("Your arrow returns and kills you!")      #L19
                break                                                      #L20
            else:                                                          #L21
                print("Your arrow continues on in room %d, silently."
                      % nextRoomNum)                                       #L22
        self.player.loseArrow()                                            #L23
    #shoot

    def process_player_actions(self):
        """
        Process user input on shooting, moving, or quitting
        """
        '''
        Algorithm
        ---------
        A01 Initialize response to empty string
        A02 Obtain valid response from user
        A03 If user entered q
            A04 Display quit message
            A05 Call player.kill()
        A06 Else if user entered m
            A07 Initialize new room location to invalid value
            A08 Obtain valid new room location from user
                A09 Display potential paths
            A10 Set player_position to new room location
        A11 Else
            A12 Call shoot()
        '''
        action_response = ''                                               #L01
        while not action_response.lower() in ['q', 's', 'm']:              #L02
            action_response = raw_input("Do you want to shoot, "
                                        "move, or quit(s/m/q)?> ")
        if action_response.lower() == 'q':                                 #L03
            self.player.kill("So long, quitter!")                          #L04
        elif action_response.lower() == 'm':                               #L05
            new_player_position = -1                                       #L06
            while new_player_position not in\
                    self.room_paths[self.player_position]:                 #L07
                print("You have tunnels only to rooms %d, %d, and %d" %    #L08
                      tuple(self.room_paths[self.player_position]))
                new_player_position = int(raw_input("Move to?> "))
            self.player_position = new_player_position                     #L09
        else:                                                              #L10
            self.shoot()                                                   #L11
    #process_player_actions

    def play(self):
        """
        Game loop
        """
        '''
        Algorithm
        ---------
        A01 While player is alive
            A02 Display current position message
            A03 If pit in room
                A04 Call player.kill with pit death message
            A05 Else if bat in room
                A06 Display "A bat takes you to another room..."
                A07 Initialize roomOffset to a random integer [1,19]
                A08 Set player position randomly
            A09 Else if Wumpus in room
                A10 Call player.kill with Wumpus death message
            A11 Else
                A12 Call describe_nearby_room_effects
                A13 Call process_player_actions
        A14 Display message for dying/winning
        '''
        while self.player.isAlive:                                         #L01
            print("You are in room %d" % self.player_position)             #L02
            if 'pit' in self.room_items[self.player_position]:             #L03
                self.player.kill("You fall into a pit and die!")           #L04
            elif 'bat' in self.room_items[self.player_position]:           #L05
                print("A bat takes you to another room...")                #L06
                roomOffset = random.randint(1, 19)                         #L07
                self.player_position =\
                    WumpusCave.reposition_randomly(self.player_position)   #L08
            elif 'Wumpus' in self.room_items[self.player_position]:        #L09
                self.player.kill("The Wumpus growls and eats you!")        #L10
            else:                                                          #L11
                self.describe_nearby_room_effects()                        #L12
                self.process_player_actions()                              #L13
        print self.player.deathMessage                                     #L14
    #play
#WumpusCave

# -----
# Main
# ----


def main():
    """
    Plays one round of Hunt-The-Wumpus with a user.
    """
    '''
    On each round the configuration of rooms and tunnels
    is the same, but the bottomless pits are placed at
    random. The initial position of the Wumpus and the
    two bats is also random. The player starts in a random
    empty room.

    REQUIREMENTS
    <See associated SMDS>

    DESIGN
    The algorithm for the main program is given below.
    <See associated partial SMDS for other aspects of the design.

    Algorithm
    ---------
    A01 Display opening salutation
    A02 Obtain whether user wants instructions from user
    A03 If user requested instructions
        A04 Call give_instructions
    A05 Setup the game
    A06 Call wumpus_cave.play()
    A07 Display exit message
    '''
    print("\n+++++++++++++++++")                                           #L01
    print("+Hunt The Wumpus+")
    print("+++++++++++++++++\n")

    user_response = raw_input("Do you want instructions (y/n)?> ")         #L02
    if user_response in ['y', 'Y']:                                        #L03
        give_instructions()                                                #L04

    wumpus_cave = WumpusCave()                                             #L05
    wumpus_cave.play()                                                     #L06

    print("\n-----------------")                                           #L07
    print("-Hunt The Wumpus-")
    print("-----------------")
#def main():

main()

#end huntTheWumpus.py
