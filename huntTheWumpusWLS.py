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
    print('to a room with bats in it you will detect a bad smell.')
    print(' ')
    print('The WUMPUS')
    print('-----------')
    print('The Wumpus is not bothered by hazards.')
    print('He has sucker feet that can grip')
    print('the sides of the bottomless pits, and he is')
    print('too big for a bat to lift. Usually he is asleep.')
    print('Two things wake him up: (1) you shooting an arrow,')
    print('or (2) you entering his room. If he wakes he either')
    print('moves to an adjacent room with probability 0.75')
    print('or stays where he is. If he ends up where you are,')
    print('he eats you; and the game is over.')
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
        self.player = Player()                                         #A01 A02
        self.room_paths, self.room_items = WumpusCave.make_room_layout()   #A03
        self.player_position = self.find_empty_room()                      #A04
    #__init__

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
        A05 For three times
            A06 Append a bat item to a random room
            A07 Append a pit item to a random room
        A08 Append a Wumpus item to a random room
        A09 Return available paths and room items
        '''

        room_paths = [None] * 20                                           #A01
        room_paths[0] = {1, 4, 7}                                          #A02
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

        room_items = [[]] * 20                                             #A03
        random.seed()                                                      #A04
        for i in range(0, 2):                                              #A05
            bat_location = random.randint(0, 19)                           #A06
            room_items[bat_location] = room_items[bat_location] + ['bat']
            pit_location = random.randint(0, 19)                           #A07
            room_items[pit_location] = room_items[pit_location] + ['pit']
        wumpus_location = random.randint(0, 19)                            #A08
        room_items[wumpus_location] = room_items[wumpus_location] + ['Wumpus']
        return room_paths, room_items                                      #A09
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
        A08 Initialize arrow
        A09 Walk room_list with nextRoomNum
            A10 Set nextRoomNum to valid room option
            A11 If Wumpus is in the room
                A12 Display win message
                A13 Call player.kill()
                A14 Break
            A15 Else if player is in the room
                A16 Display arrow kills you message
                A17 Call player.kill()
                A18 Break
            A19 Else
                A20 Display arrow no-hit message
        A21 Call player.loseArrow()
        '''
        if not self.player.hasArrows():                                    #L01
            print("You are out of arrows!")                                #L02
            return                                                         #L03
        room_list = re.compile('[ ]*[, ]?[ ]*').\
                    split(raw_input("Arrow path?> "))                 #L04 #L05
        room_list = [int(roomStr) for roomStr in room_list]           #L06 #L07

        arrow = Arrow(self.player_position, self.room_paths)               #L08
        for nextRoomNum in room_list:                                      #L09
            nextRoomNum = arrow.advance(nextRoomNum)                       #L10
            if 'Wumpus' in self.room_items[nextRoomNum]:                   #L11
                print("You have slain the Wumpus! You win!")               #L12
                self.player.kill()                                         #L13
                break                                                      #L14
            elif self.player_position == nextRoomNum:                      #L15
                print("Your arrow returns and kills you!")                 #L16
                self.player.kill()                                         #L17
                break                                                      #L18
            else:                                                          #L19
                print("Your arrow continues on in room %d, silently."
                      % nextRoomNum)                                       #L20
        self.player.loseArrow()                                            #L21
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
            print("So long, quitter!")                                     #L04
            self.player.kill()                                             #L05
        elif action_response.lower() == 'm':                               #L06
            new_player_position = -1                                       #L07
            while new_player_position not in\
                    self.room_paths[self.player_position]:                 #L08
                print("You have tunnels only to rooms %d, %d, and %d" %    #L09
                      tuple(self.room_paths[self.player_position]))
                new_player_position = int(raw_input("Move to?> "))
            self.player_position = new_player_position                     #L10
        else:                                                              #L11
            self.shoot()                                                   #L12
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
                A04 Display pit death message
                A05 Call player.kill()
            A06 Else if bat in room
                A07 Display "A bat takes you to another room..."
                A08 Initialize roomOffset to a random integer [1,19]
                A09 Add roomOffset to player_position, rolling over at 20
            A10 Else if Wumpus in room
                A11 Display "The Wumpus growls and eats you!"
                A12 Call player.kill()
            A13 Else
                A14 Call describe_nearby_room_effects
                A15 Call process_player_actions
        '''
        while self.player.isAlive:                                         #L01
            print("You are in room %d" % self.player_position)             #L02
            if 'pit' in self.room_items[self.player_position]:             #L03
                print("You fall into a pit and die!")                      #L04
                self.player.kill()                                         #L05
            elif 'bat' in self.room_items[self.player_position]:           #L06
                print("A bat takes you to another room...")                #L07
                roomOffset = random.randint(1, 19)                         #L08
                self.player_position = (self.player_position
                                        + roomOffset) % 20                 #L09
            elif 'Wumpus' in self.room_items[self.player_position]:        #L10
                print("The Wumpus growls and eats you!")                   #L11
                self.player.kill()                                         #L12
            else:                                                          #L13
                self.describe_nearby_room_effects()                        #L14
                self.process_player_actions()                              #L15
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
