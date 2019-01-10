''' successor
write an algorithm to find the next node (in order successor) of a given node
in a binary search tree

so if node value = 10, find the first smaller value and first larger value
each node has link to its parent
'''

'''
1) search for the element
1.1) if not found
'''
from classes import *
myTree2.levelPrintTree()

def findTargetNode(node, targetNumber):
    if node.value == targetNumber:
        return node
    else:
        if targetNumber > node.value:
            if node.rightNode:
                return findTargetNode(node.rightNode, targetNumber)
            else:
                return node
        else:
            if node.leftNode:
                return findTargetNode(node.leftNode, targetNumber)
            else:
                return node

def findNextNode(node):
    if not node:
        return None
    if node.rightNode:
        # find most left node in the right subtree
    else:
        # go back to parent (pop) stack until the position's parent is on the right side
        # so that the parent previously made 'left'
        # return parent 
        # so look for the first parent that made a left
        if not node.parentNode:
            return None
        current_node = node
        answer = None
        while current_node.parentNode:
            if current_node.parentNode.leftNode = current_node:
                answer = parentNode
                break;
            else:
                current_node = current_node.parentNode
        return answer
        
            

def findSuccessor(root, targetNumber):
    if not root:
        return None
    targetNode = findTargetNode(root, targetNumber)
    #parentNode = targetNode.parentNode
    '''
         [4]
       [2,  6]
    [1, 3] [5, 7]
    if parentNode.value
    '''

print findSuccessor(myTree2.rootNode, 1.5)
        