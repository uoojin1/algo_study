'''
Stack of Plates

If stack gets too high, it might fall over.
Design a data structure SetOfStacks that mimics this.

implement its push and pop
'''

class StackOfPlates:
    def __init__(self, max_height):
        self.stack_list = []
        self.max_height = max_height
        self.operation_index = 0
    def push(self, item):
        if self.stack_list == []:
            self.stack_list.append([item])
        elif self.stack_list[self.operation_index]:
            if len(self.stack_list[self.operation_index]) == self.max_height:
                self.operation_index += 1
                self.stack_list.append([item])
            else:
                self.stack_list[self.operation_index].append(item)
    def pop(self):
        if self.stack_list and self.stack_list[self.operation_index]:
            poppedElement = self.stack_list[self.operation_index].pop()
            if self.stack_list[self.operation_index] == []:
                self.stack_list.pop()
                self.operation_index -= 1

    def printMyStacks(self):
        for stack in self.stack_list:
            print ''.join(str(stack))
        print('\n')

plate_storage = StackOfPlates(3)

plate_storage.push(1)
plate_storage.push(2)
plate_storage.push(3)
plate_storage.push(1)
plate_storage.push(2)
plate_storage.push(3)
plate_storage.push(1)
plate_storage.push(2)

plate_storage.printMyStacks()

plate_storage.pop()
plate_storage.printMyStacks()

plate_storage.pop()
plate_storage.printMyStacks()

plate_storage.pop()
plate_storage.printMyStacks()

plate_storage.pop()
plate_storage.printMyStacks()

plate_storage.pop()
plate_storage.printMyStacks()

plate_storage.pop()
plate_storage.printMyStacks()

plate_storage.pop()
plate_storage.printMyStacks()



        
