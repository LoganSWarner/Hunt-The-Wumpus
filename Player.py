# ***************************************************************
# PROJECT: HuntTheWumpus
#
# FILE:	   Player.py
#
# EXEECUTION ENVIRONMENTS:
# Python 2.7 on Manjaro Linux 16
# Python 2.7 on Windows 10
#
# AUTHOR(S): Logan Warner
#
# DESCRIPTION
# Player for HuntTheWumpus
# ***************************************************************


class Player:
    def __init__(self):
        self.isAlive = True
        self.arrowCount = 5
        self.deathMessage = ''
    #__init__

    def hasArrows(self):
        return self.arrowCount > 1
    #hasArrows

    def loseArrow(self):
        self.arrowCount -= 1
    #loseArrow

    def kill(self, deathMessagePR):
        self.isAlive = False
        self.deathMessage = deathMessagePR
    #kill
#player
