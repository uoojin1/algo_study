''' Towers of Hanoi

build this toy with using stacks
'''

stack1 = range(4,0,-1)
stack2 = []
stack3 = []

''' solution

basically if moving everything from 1 to 3 is possible,
it means that we can move 1 ~ n-1 to stack 2,
move n to stack 3
and then move 1~n-1 to stack 3

so we basically need access to the last element each time
'''
print stack1, stack2, stack3

'''
1      
2      
3      
4      
'''

def solvePuzzle(height):
    def moveDisk(fromStack, toStack):
        if fromStack:
            toStack.append(fromStack.pop())
    def moveTower(height, fromPole, toPole, withPole):
        print '\nstack1: ', stack1
        print 'stack2: ', stack2
        print 'stack3: ', stack3
        if height >= 1:
            moveTower(height-1, fromPole, withPole, toPole)
            moveDisk(fromPole,toPole)
            moveTower(height-1, withPole, toPole, fromPole)
    moveTower(height, stack1, stack3, stack2)

solvePuzzle(4)
print stack1, stack2, stack3