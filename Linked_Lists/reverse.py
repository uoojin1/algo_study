'''
Reverse linked list

simple solution: using a stack
1. iterate through the linked list, at each index push the element to a stack
2. while stack not empty, pop and add the popped element into a new linked list

O(n) time, O(n) space
'''

## better solution ##

''' O(n) time,  O(1) space

use three pointers: prev, curr, next

while current not null:
    next = current.next
    current.next = prev
    prev = current
    current = next

ex) 1 -> 2 -> 3 -> 4 // we want this to be 4->3->2->1
    ^    ^
p   c    n

    initially, prev = null, current = head, next = head.next
    next = curr.next
    curr.next = prev
    prev = curr
    curr = next
'''

def reverseKGroup(self, l, k):
    if l is None or k < 2:
        return l
    
    node = l
    for i in range(k - 1):
        node = node.next
        if node is None:
            return l
    ret = node
    
    current = l
    while node:
        tail = current
        prev = None
        for i in range(k):
            if node:
                node = node.next
            _next = current.next
            current.next = prev
            prev = current
            current = _next
        tail.next = node or current
            
    return ret