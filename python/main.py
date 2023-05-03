import maze as mz
from score import ScoreboardFake, Scoreboard
from BTinterface import BTinterface

import numpy as np
import pandas
import time
import sys
import os
import threading

class RFIDthread(threading.Thread):
    def __init__(self, point_obj:Scoreboard):
        threading.Thread.__init__(self)
        self.point = point_obj

    def run(self):
        try:
            uid = BTinterface.get_UID()
            if uid > 0:
                print(f'Get UID: {uid}')
                self.point.add_UID(uid)     #upload uid to scoreboard
                print("score:", self.point.getCurrentScore())    
        except:
            pass


def main():
    maze = mz.Maze("./python/data/big_maze_111.csv") 
    point = Scoreboard("Subscribe Dhgf!!", "http://140.112.175.18:3000")
    # point = ScoreboardFake("your team name", "data/fakeUID.csv")
    interf = BTinterface()
    # TODO : Initialize necessary variables

    bfs_list = maze.nodePlanner(maze.startNode)
    cmd_str = maze.getActions(bfs_list)[1:]
    cmd_str = cmd_str + 's'
    

    print("Finish counting. Waiting for car...")

    read = interf.ser.SerialReadByte()

    while True:
        
        if read == '0x70617468':
            break
        read = str(interf.ser.SerialReadByte())
        print('current read:',end=' ')
        print(read)
    
    
    interf.ser.SerialWriteString(cmd_str)
    print(f'Send cmd_str: {cmd_str}')
    
    interf.start()
    point.socket.start_game({ 
                'gamemode': point.game, 
                'team': point.team })

    
    if (True):
        print("Mode 0: for treasure-hunting")
        # TODO : for treasure-hunting, which encourages you to hunt as many scores as possible
        while True:
            uid = interf.get_UID()
            uid = str(uid)[2:]
            if uid:
                print(f'Get UID: {uid}')
                point.add_UID(uid)     #upload uid to scoreboard
                print("score:", point.getCurrentScore()) 

        
    elif (sys.argv[1] == '1'):
        print("Mode 1: Self-testing mode.")
        # TODO: You can write your code to test specific function.
        while True:
            uid = interf.get_UID()
            uid = str(uid)[2:]
            if uid:
                print(f'Get UID: {uid}')
                point.add_UID(uid)     #upload uid to scoreboard
                print("score:", point.getCurrentScore())  


if __name__ == '__main__':
    main()
