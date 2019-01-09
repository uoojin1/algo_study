''' successor

write an algorithm to find the next node (in order successor) of a given node
in a binary search tree

so if node value = 10, find the first smaller value and first larger value

so smaller value will be the value of the rightmost child of the left subtree
larger value will be the value of the leftmost child of the right subtree
'''

from classes import *


def findNext(tree, value):
    

