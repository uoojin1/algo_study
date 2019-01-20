class listNode:
    def __init__(self, val):
        self.val = val
        self.next = None

class linkedList:
    def __init__(self, head):
        self.head = head
    def printList(self):
        node = self.head
        while node:
            print node.val
            node = node.next

''' reverse a linked list

1. we could use stack
2. we could use pointers
'''

def reverseLinkedList(head):
    node = head
    stack = []
    while node:
        stack.append(listNode(node.val))
        node = node.next
    node = stack.pop()
    newHead = node
    while stack:
        node.next = stack.pop()
        node = node.next
    return newHead


n1 = listNode(1)
n2 = listNode(2)
n3 = listNode(3)
n4 = listNode(4)

n1.next = n2
n2.next = n3
n3.next = n4

newLinkedList = linkedList(n1)

reversedList = linkedList(reverseLinkedList(n1)) 

reversedList.printList()