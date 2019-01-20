''' Given a stream of integers and a window size,
calculate the moving average of all integers in the sliding window

MovingAverage m = new MovingAverage(3)
m.next(1) = 1
m.next(10) = (1+10)/2
m.next(3) = (1+10+3)/3
m.next(5) = (10+3+5)/3
'''

class MovingAverage:
    def __init__(self, window):
        self.window = window
        self.numbers = []
        self.total = 0
    def next(self, number):
        self.numbers.insert(0, number)
        self.total += number
        if len(self.numbers) == self.window + 1:
            self.total -= self.numbers.pop()
        return float(self.total) / len(self.numbers)

myAverage = MovingAverage(3)
print myAverage.next(1)
print myAverage.next(10)
print myAverage.next(3)
print myAverage.next(5)