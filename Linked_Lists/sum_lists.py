'''
2 numbers represented by linked list
each node contains a single digit (stored in reverse order)
1's digit is at head of the list

write a function that adds two numbers and returns the sum as a linked list

ex) 123 + 23
3 -> 2 -> 1 -> None
3 -> 2 -> None
'''
from classes import *

def sum_list(list1, list2):
    node1 = list1.head
    node2 = list2.head
    answer = LinkedList()


