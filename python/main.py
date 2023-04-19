import maze as mz
from score import ScoreboardFake, Scoreboard
from BTinterface import BTinterface

import numpy as np
import pandas
import time
import sys
import os

def main():
    maze = mz.Maze("./python/data/small_maze.csv") 
    point = Scoreboard("Team Eric, Sam, and Dhgf", "ask TA for ip")
    # point = ScoreboardFake("your team name", "data/fakeUID.csv")
    interf = BTinterface()
    # TODO : Initialize necessary variables

    if (sys.argv[1] == '0'):
        print("Mode 0: for treasure-hunting")
        # TODO : for treasure-hunting, which encourages you to hunt as many scores as possible
        
    elif (sys.argv[1] == '1'):
        print("Mode 1: Self-testing mode.")
        # TODO: You can write your code to test specific function.

if __name__ == '__main__':
    main()
