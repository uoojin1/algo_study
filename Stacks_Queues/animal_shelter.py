'''
Animal Shelter holds dogs and cats, first in first out basis
either adapt oldest of either, or oldest of choice (dog or cat)
create the data structures to maintain this system
implement
- enqueue, dequeueAny, dequeueDog, dequeueCat
may use built in LinkedList data Structure
'''

class Animal:
    def __init__(self, name='Scooby Dooby Doo'):
        self.__name = name
        self.__order = None
    def getName(self):
        return self.__name
    def setOrder(self, order):
        self.__order = order
    def getOrder(self):
        return self.__order
    def isOlderThan(self, buddy):
        return self.__order >= buddy.getOrder()

class Dog(Animal):
    def __init__(self, name):
        Animal.__init__(self, name)
        self.type = "dog"

class Cat(Animal):
    def __init__(self, name):
        Animal.__init__(self, name)
        self.type = "cat"

class AnimalQueue:
    def __init__(self):
        self.dogs = []
        self.cats = []
    def dequeAny(self):
        if self.dogs == [] and self.cats == []:
            return None
        elif self.dogs == []:
            return self.cats.pop() # will reverse the insert
        elif self.cats == []:
            return self.dogs.pop()
        else:
            if self.dogs[-1].isOlderThan(self.cats[-1]):
                return self.dogs.pop()
            else:
                return self.cats.pop()
    def enqueue(self, pet):
        print pet.__class__.__name__
        if pet.__class__.__name__ == 'Dog':
            print 'this is an dog'
            self.dogs.insert(0, pet)
        else:
            self.cats.insert(0, pet)
    def dequeueDog(self):
        if self.dogs == []:
            return None
        else:
            return self.dogs.pop()
    def dequeueCat(self):
        if self.cats == []:
            return None
        else:
            return self.cats.pop()
    def printQueue(self):
        print('dog queue: ', ''.join(dog.getName()+', ' for dog in self.dogs))
        print('cat queue: ', ''.join(cat.getName()+', ' for cat in self.cats))
doggo1 = Dog('doggos moggos')
print doggo1
doggo1.setOrder(1)
doggo2 = Dog('doggi')
doggo2.setOrder(4)
cat1 = Cat('puur')
cat1.setOrder(2)
cat2 = Cat('furr')
cat2.setOrder(3)

shelterQueue = AnimalQueue()
shelterQueue.enqueue(doggo2)
shelterQueue.enqueue(cat1)
shelterQueue.enqueue(cat2)
shelterQueue.enqueue(doggo1) 

shelterQueue.printQueue()

shelterQueue.dequeueCat()
shelterQueue.printQueue()

shelterQueue.dequeAny()
shelterQueue.printQueue()

shelterQueue.dequeAny()
shelterQueue.printQueue()
