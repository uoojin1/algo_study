'''
implement an algorithm to delete a node in the middle
any node but the first and last node
singly linked list
given only access to that node
'''

from classes import *

node = list.head
prev_node = None
def deleteMiddleNode(node):
    while node is not None and node.next is not None:
        node.val = node.next.val
        prev_node = node
        node = node.next
    prev_node.next = None

list.listprint()
deleteMiddleNode(node.next.next)
list.listprint()
    
    