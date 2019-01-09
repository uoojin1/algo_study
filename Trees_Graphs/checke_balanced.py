''' check balanced

implement a function to check if a binary tree is balanced
'''

from classes import *

'''
return 1 (current height) + max (left, right)
'''

def getHeight(node):
    if not node:
        return -1
    return 1 + max(getHeight(node.leftNode), getHeight(node.rightNode))

def isBalanced(root):
    if not root:
        return True
    heightDifference = getHeight(root.leftNode) - getHeight(root.rightNode)
    if abs(heightDifference) > 1:
        return False
    else:
        return isBalanced(root.leftNode) and isBalanced(root.rightNode)

print isBalanced(myTree2.rootNode)