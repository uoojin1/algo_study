''' validate bst
check if binary tree is a binary search tree
'''

from classes import *
import sys

def validateBST(node, minimum, maximum):
    if not node:
        return True
    if node.value > maximum or node.value < minimum:
        return False
    else:
        return True and validateBST(node.leftNode) and validateBST(node.rightNode)

def isBinaryTree(node):
    if not node:
        return True
    minimum = sys.maxsize
    maximum = -sys.maxsize-1
    return validateBST(node, minimum, maximum)

print isBinaryTree(myTree.rootNode)
    