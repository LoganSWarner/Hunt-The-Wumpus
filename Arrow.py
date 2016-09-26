# ***************************************************************
# PROJECT: HuntTheWumpus
#
# FILE:	   Arrow.py
#
# EXEECUTION ENVIRONMENTS:
# Python 2.7 on Manjaro Linux 16
# Python 2.7 on Windows 10
#
# AUTHOR(S): Logan Warner
#
# DESCRIPTION
# Arrow logic for HuntTheWumpus
# ***************************************************************
import random


class Arrow:
    def __init__(self, startRoom, roomPaths):
        self.currentRoom = startRoom
        self.roomPaths = roomPaths
    #__init__

    def advance(self, nextRoomNum):
        roomOptions = list(self.roomPaths[self.currentRoom] - {self.currentRoom})
        if nextRoomNum not in roomOptions:
            nextRoomNum = self.chooseNewTargetRoom(roomOptions)
        self.currentRoom = nextRoomNum
        return nextRoomNum
    #advance

    @staticmethod
    def chooseNewTargetRoom(roomOptions):
        random.seed()
        return roomOptions[random.randint(0, 1)]
    #chooseNewTargetRoom
#Arrow
