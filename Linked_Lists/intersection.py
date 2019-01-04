'''
given 2 singly linked lists, dtermine if 2 lists intersect.
return the intersecting node
intersection is based on reference, not value

1 --> 2 --> 3 --> 4 --> 5 --> None
0 --> 6 --> ^
'''

'''
1. brute force algorithm
iterating through all of the second list for each item in the first list
O(n^2)

2. hashmap with address
as I go through the first list, I input the node's address as the key and
the data as the value (or I could just use a hashset of address)
go through the second linkedlist, check if the current element's addr is in the hash map
if yes, return the node

3. if I know or can get the length of each linked list with O(1) time,
just get the lengths, proceed the longer linked list by that difference,
at this point, iterate both lists at the same time, if meets then intersection
'''

from classes import *

def checkIntersection(input_list, input_list2):
    node = input_list.head
    address_set = set()
    while node is not None:
        address_set.add(node)
        node = node.next
    node = input_list2.head
    while node is not None:
        if node in address_set:
            print("intersection found!", node.val)
            return True
        node = node.next
    return False
    
list1.listprint()
list2.listprint()
print checkIntersection(list1, list2)