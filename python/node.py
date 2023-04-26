from enum import IntEnum
import copy

# You can get the enumeration based on integer value, or make comparison
# ex: d = Direction(1), then d would be Direction.NORTH
# ex: print(Direction.SOUTH == 1) should return False
class Direction(IntEnum):
    NORTH = 1
    SOUTH = 2
    WEST  = 3
    EAST  = 4

# Construct class Node and its member functions
# You may add more member functions to meet your needs
class Node:
    def __init__(self, index=0, Adjacency_nd=[0,0,0,0]):
        self.index = index
        self.adjacency_nd = list(Adjacency_nd)    #store the index of adjacency nodes in the sequence: North, South, West, East
        # store successor as (Node, direction to node, distance)
        self.Successors = []
        self.point = 0
        self.col = self.index // 6 + 1
        self.row = self.index % 6 if self.index % 6 > 0 else 6

    def __hash__(self) -> int:
        return self.index
    
    def __eq__(self, __value: object) -> bool:
        if not isinstance(__value, Node):
            return False
        return self.index == __value.index
    
    def getNodeCoordinate(self):
        return (self.col, self.row)

    def initSuccessors(self):
        self.Successors = list()

    def getPoint(self):
        return self.point

    def getIndex(self):
        return self.index

    def getSuccessors(self):
        return self.Successors

    def setSuccessor(self, successor, direction, length=1):
        self.Successors.append((successor, Direction(direction), int(length)))
        print("For Node {}, a successor {} is set.".format(self.index, self.Successors[-1]))
        return
    
    def copySuccessors(self, nd):
        self.Successors = copy.deepcopy(nd.getSuccessors())

    def getAdjacency(self):
        return self.adjacency_nd

    def getDirection(self, nd):
        # TODO : if nd is adjacent to the present node, return the direction of nd from the present node
		# For example, if the direction of nd from the present node is EAST, then return Direction.EAST = 4
		# However, if nd is not adjacent to the present node, print error message and return 0
        if isinstance(nd, Node):
            node_index = nd.getIndex()
        elif isinstance(nd, int):
            node_index = nd
        else:
            print("Wrong data type!")
            return 0
        
        if node_index in self.adjacency_nd:
            dir = self.adjacency_nd.index(node_index) + 1
            return Direction(dir)
        else:
            print("This node is not adjacent to the current node.")
            return 0

    def isSuccessor(self, nd):
        for succ in self.Successors:
            if succ[0] == nd: 
                return True
        return False
    
    def isDeadEnd(self) -> bool:
        adjacency = self.getAdjacency()
        nd_count = 0
        for ndIndex in adjacency:
            try:
                if isinstance(ndIndex, int) and ndIndex > 0:
                    nd_count += 1
            except:
                pass
        if nd_count <= 1:
            return True
        return False
    
    def countPoint(self, startNode):
        start_col, start_row = startNode.getNodeCoordinate()
        x_dis = abs(start_col - self.col)
        y_dis = abs(start_row - self.row)
        self.point = round((x_dis**2 + y_dis**2)**0.5)


    @staticmethod
    def reverseDir(dir):
        if dir == 1:    #From north
            return Direction(2)
        elif dir == 2:
            return Direction(1)
        elif dir == 3:
            return Direction(4)
        elif dir == 4:
            return Direction(3)
        else:
            print('Direction out of range!')
            return 0
