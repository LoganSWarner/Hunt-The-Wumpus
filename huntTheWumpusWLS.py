# ***************************************************************
# PROJECT: HuntTheWumpus
#
# FILE:	   huntTheWumpuspy
#
# PYTHON VERSION: 2.7
#
# HISTORY:
# Date		Author		    Description
# ====		======		    ===========
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

# ---------
# Functions
# ---------


def give_instructions():
    print("")
    print('The Wumpus lives in a cave of 20 rooms.')
    print('Each cave has 3 tunnels that lead to other rooms.')
    print('The Wumpus occasionally ventures out of  his room')
    print('and eats pets and children in a nearly village.')
    print('Since you are a renowned hunter you have been')
    print('commissioned to hunt and slay the Wumpus!')
    print('')
    print('Hazards!')
    print('---------')
    print('Two of the rooms have bottomless pits in them.')
    print('If you go into one of these rooms you will fall into')
    print('the pit and never be seen again! But there is a clue.')
    print('When you are in a room that has a tunnel that connects')
    print('to a room with a bottomless pit you will feel a draft.')
    print(' ')
    print('The Wumpus shares his cave with two giant bats.')
    print('These giant bats live in two distinct rooms. If you')
    print('so much as enter one of these rooms, a giant bat will')
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
# def give_instructions()


def make_room_layout():
    """Build a representation of the rooms for the game rooms
    and place non-player objects"""
    '''
    Algorithm
    ---------
    A01 Create a size 20 list, room_paths, to represent paths
    A02 Populate room_paths according to possible vertices to go to for each
        index, based on numbering a dodecahedron in a spiral manner
    A03 Create a size 20 list, room_items, to represent room contents
    A04 Populate room_items with, randomly-placed, 2 bats & pits
    A05 Place, randomly, a Wumpus into room_items
    '''

    room_paths = [None] * 20                                               # A01
    room_paths[0] = [1, 2, 3]                                              # A02
    room_paths[1] = [0, 4, 5]
    room_paths[2] = [0, 6, 7]
    room_paths[3] = [0, 8, 9]
    room_paths[4] = [1, 9, 10]
    room_paths[5] = [1, 6, 11]
    room_paths[6] = [2, 5, 12]
    room_paths[7] = [2, 8, 13]
    room_paths[8] = [3, 7, 14]
    room_paths[9] = [3, 4, 15]
    room_paths[10] = [4, 11, 16]
    room_paths[11] = [5, 10, 17]
    room_paths[12] = [6, 13, 17]
    room_paths[13] = [7, 12, 18]
    room_paths[14] = [8, 15, 18]
    room_paths[15] = [9, 14, 16]
    room_paths[16] = [10, 15, 19]
    room_paths[17] = [11, 12, 19]
    room_paths[18] = [13, 14, 19]
    room_paths[19] = [16, 17, 18]

    room_items = [[]] * 20                                                 # A03
    random.seed()                                                          # A04
    for i in range(1, 2):
        room_items[random.randint(0, 19)] += ['bat']
        room_items[random.randint(0, 19)] += ['pit']
    room_items[random.randint(0, 19)] += ['Wumpus']                        # A05
    print room_items
    return room_paths, room_items
# def makeRoomLayout


def find_empty_room(room_items):
    for index, items in enumerate(room_items):
        if items is []:
            return index
#def find_empty_room

# -----
# Main
# ----
def main():
    """Plays one round of Hunt-The-Wumpus with a user."""
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
    A01 Display opening salutation;
    A02 Obtain request from user for instructions (usrChoice):
            Do you want instructions (y/n)>
    A03 If (usr requested instructions) {
            Display <instructions>
    A04 Set up the rooms
    A05 Place the user in an empty room
    A06 Obtain action from user
    A07 Perform action
        A08 Shoot
        A09 Move rooms
    A10 Change room state
    '''

    print("")                                                             # A01
    print("+++++++++++++++++")
    print("+Hunt The Wumpus+")
    print("+++++++++++++++++\n")

    give_instructions()                                                    # A02

    room_paths, room_items = make_room_layout()
    player_position = find_empty_room(room_items)

    print("-----------------")
    print("-Hunt The Wumpus-")
    print("-----------------")
# def main():

main()

# end huntTheWumpus.py
