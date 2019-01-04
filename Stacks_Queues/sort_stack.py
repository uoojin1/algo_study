'''
write a program to sort a stack such that the smallest items are on the top
you may only use additional stack - push, pop, peek, is empty
'''

'''
5
3
2
6
1
8

if I could use a int to hold a value, then i could do something like

back and forth
'''

from classes import *

sort_this_stack = Stack([5,2,1,6,3,25,7,2,5,2,1])
def sortStack(input_stack):
    sorted_stack = Stack()
    holder = None
    while not input_stack.isEmpty():
        top_of_input_stack = input_stack.peek()
        top_of_sorted_stack = sorted_stack.peek()
        if top_of_input_stack <= top_of_sorted_stack or top_of_sorted_stack is None:
            sorted_stack.push(input_stack.pop())
        else:
            holder = input_stack.pop()
            while sorted_stack.peek() <= holder and sorted_stack.peek() is not None:
                input_stack.push(sorted_stack.pop())
            sorted_stack.push(holder)
    return sorted_stack

print sortStack(sort_this_stack).items
