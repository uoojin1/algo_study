'''
Check if linkedlist is a palindrome

using a stack, place all the elements into the stack in order
use a fast runner and slow runner to target the center position

1 2 3 4 5 6
^ ^ ^ ^
^   ^   ^   ^
^   ^   ^   ^

thus, if fast runner reaches null, it means there are even numbers and 
at that moment, the slow runner is at the start of second half

if fast runner is not null but if its .next == Null, there are odd numbers
and at that moment, the slow runner is at the exact halfpoint
'''

from classes import *

def isPalindrome(input_list):
    input_stack = [] # using it as a stack
    fast_runner = input_list.head;
    slow_runner = fast_runner;
    while fast_runner is not None and fast_runner.next is not None:
        input_stack.append(slow_runner.val)
        slow_runner = slow_runner.next
        fast_runner = fast_runner.next.next
    if fast_runner is not None: # odd numbers , so skip one
        slow_runner = slow_runner.next
    if fast_runner is None: # even numbers, current slow runner is N/2+1
        while slow_runner is not None:
            if slow_runner.val != input_stack.pop():
                return False
            slow_runner = slow_runner.next
    return True

# palindrome_list.listprint()
print isPalindrome(palindrome_list)