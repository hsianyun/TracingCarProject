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
    maze = mz.Maze("./python/data/small_maze.csv") 
    point = Scoreboard("Team Eric, Sam, and Dhgf", "ask TA for ip")
    # point = ScoreboardFake("your team name", "data/fakeUID.csv")
    interf = BTinterface()
    # TODO : Initialize necessary variables
    while(interf.ser.SerialReadString() != 'p'):
        pass
    bfs_list = maze.BFS_2(3,48)
    cmd_str = maze.getActions(bfs_list)

    interf.start()
    interf.ser.SerialWriteString(cmd_str)
    if (sys.argv[1] == '0'):
        print("Mode 0: for treasure-hunting")
        # TODO : for treasure-hunting, which encourages you to hunt as many scores as possible
        

        
    elif (sys.argv[1] == '1'):
        print("Mode 1: Self-testing mode.")
        # TODO: You can write your code to test specific function.
        while True:
            uid = BTinterface.get_UID()
            if uid:
                print(f'Get UID: {uid}')
                point.add_UID(uid)     #upload uid to scoreboard
                print("score:", point.getCurrentScore())  


if __name__ == '__main__':
    main()
