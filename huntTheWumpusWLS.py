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

# ---------
# Functions
# ---------
def giveInstructions():
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
    <rest to be supplied>
    '''

    print("")  # A01
    print("+++++++++++++++++")
    print("+Hunt The Wumpus+")
    print("+++++++++++++++++\n")

    giveInstructions()  # A02

    print("-----------------")
    print("-Hunt The Wumpus-")
    print("-----------------")
# def main():

main()

# end huntTheWumpus.py
