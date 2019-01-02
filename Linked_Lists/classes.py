class Node:
    def __init__(self, val):
        self.val = val
        self.next = None ## points to nothing at beginning

class LinkedList:
    def __init__(self):
        self.head = None
    def listprint(self):
        if self.head == None:
            return("nothing is in the list")
        node = self.head
        while node is not None:
            print(node.val)
            node = node.next

node1 = Node(3)
node2 = Node(4)
node3 = Node(5)
node4 = Node(6)
node5 = Node(7)
node6 = Node(8)

list = LinkedList()
list.head = node1
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node6

# print(list.listprint())