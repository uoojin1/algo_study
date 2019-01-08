'''
Design a stack which, in addition to push and pop, has a function min()
which returns the minimum element.
push, pop, min should all operate in O(1) time
'''

class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []
    def pop(self):
        poppedElement = self.stack.pop()
        if self.min_stack and poppedElement == self.min_stack[-1]:
            self.min_stack.pop()
        return poppedElement
    def push(self, item):
        self.stack.append(item)
        if self.min_stack:
            current_min = self.min_stack[-1]
            if item <= current_min:
                self.min_stack.append(item)
        else:
            self.min_stack.append(item)
    def getMin(self):
        if self.min_stack:
            return self.min_stack[-1]
        else :
            return None
    def peek(self):
        if self.stack:
            return self.stack[-1]
        else:
            return None
    def printStack(self):
        stack_string = ''
        for item in self.stack:
            stack_string += ' ' + str(item)
        print stack_string

myMinStack = MinStack();
myMinStack.push(9)
myMinStack.push(3)
myMinStack.push(2)
myMinStack.push(4)
myMinStack.push(3)
myMinStack.push(3)
myMinStack.push(3)
myMinStack.push(2)
myMinStack.push(-1)
myMinStack.push(6)


myMinStack.printStack()
print myMinStack.getMin()

myMinStack.pop()
print myMinStack.getMin()

myMinStack.pop()
print myMinStack.getMin()

myMinStack.pop()
print myMinStack.getMin()
