''' Minimal Tree

given a sorted (increasing) array with unique integer elements,
write an algorithm to create a binary search tree with minimal height
'''

'''
   1
  2 3
4 5 6 7
always think recursively!
1. put the middle element in the sorted array into the binary tree
2. split the array in 2 halves
pass the splitted array in the the recursive call and repeat

* if odd, just pick the middle node, if even, pick the right from the middle
if len = 3 (1, 2, 3)
3/2 = 1 (index points at 2 so it is correct)
lf len = 4 (1, 2, 3, 4)
4/2 = 2 (index points at 3 so it is also correct)
'''

from classes import *

sorted_unique_integers = [1, 2, 3, 4, 5, 6, 7]

def createMinimalBSTHelper(input_array):
    if not input_array:
        return None
    if len(input_array) == 1:
        return TreeNode(input_array[0])
    node = TreeNode(input_array[len(input_array)/2])
    node.leftNode = createMinimalBST(input_array[0:len(input_array)/2])
    node.rightNode = createMinimalBST(input_array[len(input_array)/2+1:])
    return node


def createMinimalBST(input_array):
    return createMinimalBSTHelper(input_array)

root = createMinimalBST(sorted_unique_integers)
myTree = Tree(root)
myTree.levelPrintTree()
