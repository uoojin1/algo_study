''' Route Between Nodes

Given a directed graph, design an algorithm to find out wheter there is a route between two nodes
'''

from classes import *

point1 = gNode1
point2 = gNode9

def routeBetweenNodes(point1, point2):
    if point1 == point2:
        return True
    else:
        point1.visited = True
        found = False
        for adjNode in point1.adjacentNodes:
            print 'adjacent Node: ' + str(adjNode.value) + ' visited: ', adjNode.visited
            if not adjNode.visited:
                found = found or routeBetweenNodes(adjNode, point2)
        return found

print routeBetweenNodes(point1, point2)

