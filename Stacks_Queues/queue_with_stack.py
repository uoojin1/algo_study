'''
implement a MyQueue class which implements a queue with 2 stacks
'''

'''
Queue: first in first out
Stack: first in last out

obviously we first have to insert to stack1 for enqueue, b/c we can't do anything else
then if we want to dequeue, we need to get the oldest element (which is at the bottom of stack1)
so we can first put everything in stack1 to stack2 using stack2.push(stack1.pop())
until stack1 is empty
then, we can pop from stack2 and return that --> completion of dequeue
'''

class MyQueue:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []
    def enqueue(self, item):
        self.stack1.append(item)
    def dequeue(self):
        # you would only transfer all the elements if stack2 is empty, otherwise mixed order
        if len(self.stack2) == 0:
            while len(self.stack1) != 0:
                self.stack2.append(self.stack1.pop())
        return self.stack2.pop()

myQueue = MyQueue()

print(' --- before enqueue --- ')
print myQueue.stack1
print myQueue.stack2
myQueue.enqueue(1)
myQueue.enqueue(2)
myQueue.enqueue(3)
myQueue.enqueue(4)
myQueue.enqueue(5)
print(' --- after enqueue --- ')
print myQueue.stack1
print myQueue.stack2
myQueue.dequeue()
print(' --- after first dequeue --- ')
print myQueue.stack1
print myQueue.stack2
myQueue.dequeue()
myQueue.dequeue()
print(' --- after thrid dequeue --- ')
print myQueue.stack1
print myQueue.stack2


