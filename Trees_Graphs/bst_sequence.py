'''bst sequence
bst was created from reading an integer array from left to right,
inserting the index element at each step.

given a bst, find all possible array permutations that give the bst
'''

from classes import *

# myTree2.levelPrintTree()

'''
main idea is that a node has to be inserted before its children.
lets think this recursively.

     4      #4
   2   6    #426, 462
  1 3 5 7

at 1, [[1]] // path == [3]
at 3, [[3]]
at 2, [[2,1,3],[2,3,1]]
'''

def helper(node):
    ret = []


# def helper(node):
#     if not node:
#         return [[]]
#     if not node.leftNode and not node.rightNode:
#         return [[node.value]]
#     ret = []
#     for path in helper(node.leftNode):
#         ret.append([node.value]+path)
#     for path in helper(node.rightNode):
#         ret.append([node.value]+path)
#     return ret

def findBstPermutation(tree):
    if not tree and not tree.rootNode:
        return None
    print tree.rootNode.value
    return helper(tree.rootNode)

print findBstPermutation(myTree2)

# myTree2.levelPrintTree()
