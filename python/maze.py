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
        self.deadends = list()
        for node in self.nodes:
            index = node.getIndex()
            self.nd_dict[index] = node
            if node.isDeadEnd():
                self.deadends.append(index)


    def getStartPoint(self):
        if (len(self.nd_dict) < 2):
            print("Error: the start point is not included.")
            return 0
        return self.nd_dict[1]

    def getNodeDict(self):
        return self.nd_dict
    
    def getDeadend(self):
        return self.deadends

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
                    if not cur.isSuccessor(self.nd_dict[nd]):
                        # self.nd_dict[nd].copySuccessors(cur)
                        self.nd_dict[nd].setSuccessor(cur, Direction(adjacency_nd.index(nd)+1), cur.getSuccessors()[-1][-1] +1)
                        bfs_queue.append(self.nd_dict[nd])
                        search_count += 1
                except:
                    pass

            if search_count == 0:   #find deadend
                node_sequence = [cur]
                while True:
                    if cur == start_node:
                        break
                    last_nd = cur.getSuccessors()[-1][0]
                    node_sequence = [last_nd] + node_sequence
                    cur = last_nd
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
                node_sequence = [cur]
                while True:
                    if cur == start_node:
                        break
                    last_nd = cur.getSuccessors()[-1][0]
                    node_sequence = [last_nd] + node_sequence
                    cur = last_nd
                return node_sequence
            
            adjacency_nd = list(cur.getAdjacency())
            for nd in adjacency_nd:
                try:
                    nd = int(nd)
                    if not cur.isSuccessor(self.nd_dict[nd]):
                        # self.nd_dict[nd].copySuccessors(cur)
                        self.nd_dict[nd].setSuccessor(cur, Direction(adjacency_nd.index(nd)+1), cur.getSuccessors()[-1][-1] +1)
                        bfs_queue.append(self.nd_dict[nd])
                except:
                    pass

        return None

    def getAction(self, car_dir, nd_from:Node, nd_to:Node):
        # TODO : get the car action
        # Tips : return an action and the next direction of the car if the nd_from is the Successor of nd_to
		# If not, print error message and return 0
        if not nd_to.isSuccessor(nd_from):
            print(f"Node{nd_from.getIndex()} is not the Successor of the node{nd_to.getIndex()}")
            print(nd_to.getSuccessors()[-1][0].getIndex())
            return 0
        
        next_dir  = nd_from.getDirection(nd_to)
        if next_dir == 0: return 0

        if car_dir == next_dir: return 'f'
        elif car_dir == 1:    #car facing north
            if next_dir == 2: return 'b'
            elif next_dir == 3: return 'l'
            elif next_dir == 4: return 'r'
        elif car_dir == 2:
            if next_dir == 1: return 'b'
            elif next_dir == 3: return 'r'
            else: return 'l'
        elif car_dir == 3:
            if next_dir == 1: return 'r'
            elif next_dir == 2: return 'l'
            else: return 'b'
        elif car_dir == 4:
            if next_dir == 1: return 'l'
            elif next_dir == 2: return 'r'
            else: return 'b'
        return 0

    def getActions(self, nodes:list):
        # TODO : given a sequence of nodes, return the corresponding action sequence
        # Tips : iterate through the nodes and use getAction() in each iteration
        cmd_str = 'f'
        for i in range(1,len(nodes)-1):
            cmd_str += self.getAction(nodes[i].getSuccessors()[-1][1], nodes[i], nodes[i+1])
        return cmd_str

    def actions_to_str(self, actions):
        # cmds should be a string sequence like "fbrl....", use it as the input of BFS checklist #1
        cmd = "fbrls"
        cmds = ""
        for action in actions: cmds += cmd[action-1]
        print(cmds)
        return cmds
    
    def strategy(self, start_nd, went:list, node_walk:list):
        if len(went) != len(self.deadends):
            dist = 100
            next_nd = 0
            for i in self.getDeadend():
                if i not in went:
                    if len(self.BFS(start_nd, i)) < dist and start_nd.getpoint < i.countpoint:
                        next_nd = i #index of node
            went += [next_nd]
            node_walk += [next_nd]
            return(self.strategy(next_nd, went:list, node_walk))
        else:
            return node_walk
        
    def initNodes(self):
        for node in self.nodes:
            node.initSuccessors()

    def strategy_2(self, nd_from, nd_to):
        return self.BFS_2(nd_from, nd_to)

    