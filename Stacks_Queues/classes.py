class Stack:
    def __init__(self, initial_list = []):
        self.items = initial_list
    def isEmpty(self):
        return self.items == []
    def push(self, item):
        self.items.append(item)
    def pop(self):
        if len(self.items) == 0:
            return None
        else:
            return self.items.pop()
    def peek(self):
        if len(self.items) > 0:
            return self.items[-1]
        else:
            return None
    def size(self):
        return len(self.items)

class Queue:
    def __init__(self, initial_list = []):
        self.items = initial_list
    def isEmpty(self):
        return self.items == []
    def enqueue(self, item):
        self.items.insert(0, item) # insert in reverse order
    def dequeue(self):
        return self.items.pop()
    def size(self):
        return len(self.items)