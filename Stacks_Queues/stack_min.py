# '''
# Design a stack which, in addition to push and pop, has a function min()
# which returns the minimum element.
# push, pop, min should all operate in O(1) time
# '''

# class MinStack:
#     def __init__(self):
#         self.stack = []
#         self.min_stack = []
#     def pop(self):
#         poppedElement = self.stack.pop()
#         if self.min_stack and poppedElement == self.min_stack[-1]:
#             self.min_stack.pop()
#         return poppedElement
#     def push(self, item):
#         self.stack.append(item)
#         if self.min_stack:
#             current_min = self.min_stack[-1]
#             if item <= current_min:
#                 self.min_stack.append(item)
#         else:
#             self.min_stack.append(item)
#     def getMin(self):
#         if self.min_stack:
#             return self.min_stack[-1]
#         else :
#             return None
#     def peek(self):
#         if self.stack:
#             return self.stack[-1]
#         else:
#             return None
#     def printStack(self):
#         stack_string = ''
#         for item in self.stack:
#             stack_string += ' ' + str(item)
#         print stack_string

# myMinStack = MinStack();
# myMinStack.push(9)
# myMinStack.push(3)
# myMinStack.push(2)
# myMinStack.push(4)
# myMinStack.push(3)
# myMinStack.push(3)
# myMinStack.push(3)
# myMinStack.push(2)
# myMinStack.push(-1)
# myMinStack.push(6)


# myMinStack.printStack()
# print myMinStack.getMin()

# myMinStack.pop()
# print myMinStack.getMin()

# myMinStack.pop()
# print myMinStack.getMin()

# myMinStack.pop()
# print myMinStack.getMin()


class MinimumStack:
    def __init__(self):
        self.stack = []
        self.minimum_stack = []
    def pop(self):
        if not self.stack:
            return None
        poppedElement = self.stack.pop()
        if self.minimum_stack and poppedElement == self.minimum_stack[-1]:
            self.minimum_stack.pop()
        print '\npop!'
        print 'self.stack: ', [item for item in self.stack]
        print 'self.min_stack', [item for item in self.minimum_stack] 
        return poppedElement
        
    def push(self, item):
        self.stack.append(item)
        if self.minimum_stack:
            current_minimum = self.minimum_stack[-1] # get current min
            if item <= current_minimum:
                print 'here??'
                self.minimum_stack.append(item)
        else:
            self.minimum_stack.append(item)
        print self.minimum_stack
    def getMinimum(self):
        if self.minimum_stack:
            return self.minimum_stack[-1]
        else:
            return None

def minimumOnStack(operations): 
    myMinStack = MinimumStack()
    result = []
    for operation in operations:
        op = operation.split(" ");
        if len(op) == 2:
            print 'testing', int(op[1])
            myMinStack.push(int(op[1]))
        else:
            if op[0] == 'min':
                result.append(myMinStack.getMinimum())
            else:
                myMinStack.pop()
    return result



operations = ["push 10", 
 "min", 
 "push 5", 
 "min", 
 "push 8", 
 "min", 
 "pop", 
 "min", 
 "pop", 
 "min"]

print minimumOnStack(operations);