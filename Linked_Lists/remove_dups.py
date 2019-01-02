class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    def printList(self):
        if self.head == None:
            print("nothing is in the list")
        else:
            node = self.head
            while(node is not None):
                print(node.val)
                node = node.next

Node1 = Node(1)
Node2 = Node(2)
Node3 = Node(3)
Node4 = Node(1)
Node5 = Node(6)

list = LinkedList()
list.head = Node1
Node1.next = Node2
Node2.next = Node3
Node3.next = Node4
Node4.next = Node5

# print(list.printList())

'''
write a code to remove duplicates from an unsorted linked list
'''

'''
put each element in hashset, if exists in set, remove current element
'''

def remove_dup(list):
    node = list.head
    value_set = set()
    value_set.add(node.val)

    while node.next is not None:
        if node.next.val in value_set:
            node.next = node.next.next
        else:
            value_set.add(node.val)
        node = node.next
    return list
remove_dup(list).printList()
