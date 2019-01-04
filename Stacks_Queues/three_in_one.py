'''
Three in One. Describe how you could use a single array to implement
three stacks
'''

'''
probably instead of storing just the data, have an array of object
that holds the value and the index of the stack below the top item

so.. for example
[{value: 3, prev: None}, {value: 6, prev: None}, {value:4, prev: 0} ...]

however, this would not work b/c pop can create holes in the middle
'''

''' SMART SOLUTION
need to use 2 additional arrays and 1 int
1. top_of_stack
2. next_index
3. next_available

top_of_stack would hold the index of top of each array
[-1, 2, 1] // stack 1 empty, stack 2 index 2, stack 3 index 1

next_index would hold the index of the next element when empty, 
and will hold the previous index when occupied

stacks.push(0,3) stacks.push(0,3)
stacks.push(1,7)

at this point, 
stack_data = [3, 3, 7, None, ....]
                 ^  ^
max of stack #   0  1
thus, top_of_stack = [1,2,-1] and next_index = [-1, 0, -1], next_available = 4

stacks.pop(0)

at this point, 
stack_data = [3, 0, 7]
              ^     ^
max of stack #0     1
thus, top_of_stack = [0,1,-1], next_index=[-1,4,-1], next_available = 1

'''
from classes import * 

class threeStacksInOneArray:
    def __init__(self, N=3, array_size=10):
        self.N = N
        self.array_size = array_size
        self.stack_data = [None]*array_size
        self.next_available = 0 # pointing at the start of array
        self.top_of_stack = [-1]*N
        self.next_or_previous_index = range(1,array_size)
    def push(self, stack_number, value):
        index = self.next_available
        self.stack_data[index] = value
        # setting the n/p index to point to the previous index
        self.next_available = self.next_or_previous_index[index]
        self.next_or_previous_index[index] = self.top_of_stack[stack_number]
        self.top_of_stack[stack_number] = index
    def pop(self, stack_number):
        if self.top_of_stack[stack_number] == -1:
            print("nothing in stack", stack_number)
            return
        index = self.top_of_stack[stack_number]
        self.top_of_stack[stack_number] = self.next_or_previous_index[index]
        self.next_or_previous_index[index] = self.next_available
        self.next_available = index
        self.stack_data[index] = None # remove that number

versatileArray = threeStacksInOneArray(3, 10)
print versatileArray.stack_data

versatileArray.push(0, 1)
versatileArray.push(0, 1)
versatileArray.push(0, 1)

versatileArray.push(2, 7)
versatileArray.push(2, 7)

versatileArray.pop(0)
versatileArray.push(1, 13)
versatileArray.push(0, 44)
print versatileArray.stack_data
print versatileArray.next_or_previous_index
print versatileArray.next_available
print versatileArray.top_of_stack


