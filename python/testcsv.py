# import pandas as pd

# filepath = r"d:\Coding_Projects\sample_code\python\data\small_maze.csv"
# raw_data = pd.read_csv(filepath).values
# print(raw_data)
# print(isinstance(raw_data[0][1], int))
# print(type(raw_data[0][1]))
# # from enum import IntEnum

# # class Direction(IntEnum):
# #     NORTH = 1
# #     SOUTH = 2
# #     WEST  = 3
# #     EAST  = 4

# # d = Direction(1)
# # print(d)

from maze import Maze
import os
filepath = os.path.join(os.getcwd(), r'.\python\data\big_maze_111.csv')
maze1 = Maze(filepath)
# bfs_list = maze1.BFS_2(3,48)
# print(maze1.nd_dict)
# print(maze1.getDeadend())
node_list = maze1.nodePlanner(maze1.startNode)
print(node_list)
bfs_index = [nd.getIndex() for nd in node_list ]
print(bfs_index)
cmd = maze1.getActions(node_list)
print(cmd)