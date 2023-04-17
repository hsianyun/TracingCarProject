from node import *
import numpy as np
import csv
import pandas as pd
from enum import IntEnum
import math


class Action(IntEnum):
    ADVANCE = 1
    U_TURN = 2
    TURN_RIGHT = 3
    TURN_LEFT = 4
    HALT = 5


class Maze:
    def __init__(self, filepath):
        # TODO : read file and implement a data structure you like
		# For example, when parsing raw_data, you may create several Node objects.  
		# Then you can store these objects into self.nodes.  
		# Finally, add to nd_dict by {key(index): value(corresponding node)}
        self.raw_data = pd.read_csv(filepath).values    #generate lists
        self.nodes = [Node(int(raw_node[0]), raw_node[1:5]) for raw_node in self.raw_data]
        self.nd_dict = dict()  # key: index, value: the correspond node
        for node in self.nodes:
            self.nd_dict[node.getIndex()] = node

    def getStartPoint(self):
        if (len(self.nd_dict) < 2):
            print("Error: the start point is not included.")
            return 0
        return self.nd_dict[1]

    def getNodeDict(self):
        return self.nd_dict

    def BFS(self, nd:Node):
        # TODO : design your data structure here for your algorithm
        # Tips : return a sequence of nodes from the node to the nearest unexplored deadend
        if isinstance(nd, Node):
            start_node = nd
        elif isinstance(nd, int):
            start_node = self.nd_dict[nd]
        else:
            print("Error: Parameter 'nd' wrong type!")
            return 0
        
        bfs_queue = [start_node]
        start_node.Successors=[(None, None, 0)] #initiallize the start node

        while len(bfs_queue) > 0:
            cur = bfs_queue.pop(0)
            adjacency_nd = list(cur.getAdjacency())
            search_count = 0
            for nd in adjacency_nd:
                try:
                    nd = int(nd)
                    if (not cur.isSuccessor(self.nd_dict[nd])) and len(self.nd_dict[nd].getSuccessors()) == 0:
                        self.nd_dict[nd].copySuccessors(cur)
                        self.nd_dict[nd].setSuccessor(cur, Direction(adjacency_nd.index(nd)+1), cur.getSuccessors()[-1][-1] +1)
                        bfs_queue.append(self.nd_dict[nd])
                        search_count += 1
                except:
                    pass

            if search_count == 0:   #find deadend
                node_sequence = [successor[0] for successor in cur.Successors[1:]] + [cur]
                return node_sequence

            
        return None

    def BFS_2(self, nd_from, nd_to):
        # TODO : similar to BFS but with fixed start point and end point
        # Tips : return a sequence of nodes of the shortest path
        if isinstance(nd_from, Node):
            start_node = nd_from
            end_node = nd_to
        elif isinstance(nd_from, int):
            start_node = self.nd_dict[nd_from]
            end_node = self.nd_dict[nd_to]
        else:
            print("Parameter 'nd' wrong type!")
            return 0
        
        bfs_queue = [start_node]
        start_node.Successors=[(None, None, 0)] #initiallize the start node

        while len(bfs_queue) > 0:
            cur = bfs_queue.pop(0)

            if cur == end_node:
                node_sequence = [successor[0] for successor in cur.Successors[1:]] + [cur]
                return node_sequence
            
            adjacency_nd = list(cur.getAdjacency())
            for nd in adjacency_nd:
                try:
                    nd = int(nd)
                    if (not cur.isSuccessor(self.nd_dict[nd])) and len(self.nd_dict[nd].getSuccessors()) == 0:
                        self.nd_dict[nd].copySuccessors(cur)
                        self.nd_dict[nd].setSuccessor(cur, Direction(adjacency_nd.index(nd)+1), cur.getSuccessors()[-1][-1] +1)
                        bfs_queue.append(self.nd_dict[nd])
                except:
                    pass

        return None

    def getAction(self, car_dir, nd_from, nd_to):
        # TODO : get the car action
        # Tips : return an action and the next direction of the car if the nd_to is the Successor of nd_to
		# If not, print error message and return 0
        return None

    def getActions(self, nodes):
        # TODO : given a sequence of nodes, return the corresponding action sequence
        # Tips : iterate through the nodes and use getAction() in each iteration
        return None

    def actions_to_str(self, actions):
        # cmds should be a string sequence like "fbrl....", use it as the input of BFS checklist #1
        cmd = "fbrls"
        cmds = ""
        for action in actions: cmds += cmd[action-1]
        print(cmds)
        return cmds

    def strategy(self, nd):
        return self.BFS(nd)

    def strategy_2(self, nd_from, nd_to):
        return self.BFS_2(nd_from, nd_to)

    