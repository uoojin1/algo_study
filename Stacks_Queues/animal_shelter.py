'''
Animal Shelter holds dogs and cats, first in first out basis
either adapt oldest of either, or oldest of choice (dog or cat)
create the data structures to maintain this system
implement
- enqueue, dequeueAny, dequeueDog, dequeueCat
may use built in LinkedList data Structure
'''

class Animal:
    def __init__(self, name, time_in=None):
        self.name = name
        self.time_in = time_in
    def getTimeIn(self):
        return self.time_in
    def setTimeIn(self, time_in):
        self.time_in = time_in
    def isOlderThan(animal):
        return this.time_in > animal.getTimeIn()
class Dog(Animal):
    def __init__(self, name="", time_in=0):
        Animal.__init__(self, name, time_in)
        self.type = "dog"
class Cat(Animal):
    def __init__(self, name="", time_in=0):
        Animal.__init__(self, name, time_in)
        self.type = "cat"

dog1 = Dog("doggy")
print dog1.name
print dog1.time_in