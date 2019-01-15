''' Call Center

imagine a callcenter with 3 levels of employees
1. respondent
2. manager
3. director

incoming telephone call must be first allocated to a respondent
who is free.
if the respondent can't handle the call, he must escalate the call
to a manager.
If manager is not free or not able to handle it, then the call
should be escalated to a director

Design the classes and datastructures for this problem.

implement a method dispatchCall() which assigns a call to the first
available employee
'''

'''
from reading the question, it seems like the call cannot be holded
so, if an employee is busy, the call must go to a different employee
'''

class Employee:
    def __init__(self, name, number, level='respondent'):
        self.name = name
        self.number = number
        self.occupied = False
        self.level = level
    def isBusy(self):
        return self.occupied
    def getName(self):
        return self.name
    def getNumber(self):
        return self.number
    def getLevel(self):
        return self.level

class Respondent(Employee):
    def __init__(self, name, number):
        Employee.__init__(name, number, 'respondent')

class Manager(Employee):
    def __init__(self, name, number):
        Employee.__init__(name, number, 'manager')

class Director(Employee):
    def __init__(self, name, number):
        Employee.__init__(name, number, 'director')

class AvailableEmployees:
    def __init__(self, type):
        self.queue = []
        self.type = type
    def enqueue(self, person):
        self.queue = self.queue.insert(0, person)
    def dequeue(self):
        return self.queue.pop()
    def isEmpty(self):
        return len(self.queue) == 0

class AvailableRespondents(AvailableEmployees):
    def __init__(self):
        AvailablePeople.__init__(self, 'respondent')

class AvailableManagers(AvailableEmployees):
    def __init__(self):
        AvailableManagers.__init__(self, 'manager')

class AvailableDirector(AvailableEmployees):
    def __init__(self):
        AvailableDirector.__init__(self, 'manager')

class Call:
    def __init__(self, phoneNumber):
        self.phoneNumber = phoneNumber
    def findNextAvailable(self):

class CallCenter:
    def __init__(self):
        self.managers = []
        self.directors = []
        self.respondents = []
    def findNextAvailable(self):
        

