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

node1 = Node(52)
node2 = Node(44)
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

node11 = Node(3)
node12 = Node(4)
node13 = Node(5)
node14 = Node(6)
node15 = Node(7)

list1 = LinkedList()
list1.head = node11
node11.next = node12
node12.next = node13
node13.next = node14
node14.next = node15

list2 = LinkedList()
list2.head = node1
node1.next = node2
node2.next = node13
node13.next = node14
node14.next = node15

palindrome_list = LinkedList()
node111 = Node(2)
node112 = Node(3)
node113 = Node(7)
node114 = Node(3)
node115 = Node(2)
palindrome_list.head = node111
node111.next = node112
node112.next = node113
node113.next = node114
node114.next = node115


# print(list.listprint())