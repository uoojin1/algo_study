''' List of Depths

given binary tree, create a linked lists of all the nodes at each depth
'''

from classes import *

def listOfDepths(input_tree):
    if not input_tree:
        return []
    totalList = []
    currLevel = [input_tree]
    while currLevel:
        print [node.value for node in currLevel]
        totalList.append(currLevel)
        nextLevel = []
        for node in currLevel:
            if node.leftNode:
                nextLevel.append(node.leftNode)
            if node.rightNode:
                nextLevel.append(node.rightNode)
        currLevel = nextLevel
    return totalList

myList = listOfDepths(myTree.rootNode)

def printMyList(input_list):
    if not input_list:
        return
    for list in input_list:
        printMyList(list)



