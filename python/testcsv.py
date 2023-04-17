import pandas as pd

filepath = r"d:\Coding_Projects\sample_code\python\data\small_maze.csv"
raw_data = pd.read_csv(filepath).values
print(raw_data)
nodes = [(raw_node[0], raw_node[1:5]) for raw_node in raw_data]
print(nodes)
# from enum import IntEnum

# class Direction(IntEnum):
#     NORTH = 1
#     SOUTH = 2
#     WEST  = 3
#     EAST  = 4

# d = Direction(1)
# print(d)