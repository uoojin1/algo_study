''' find celebrity

everyone knows celebrity
celebrity doesn't know anyone

you have api knows(a, b) which returns true if person a knows person b

find celebrity with minimal api calls
'''

def findCelebrity(n):
    candidate = 0
    for i in range(1, n):
        if knows(candidate, i): # if candidate knows someone, he's not a celeb
            candidate = i # just set the i to the new candidate b/c candidate can be known by anyone
    # at the end of loop, we have a candidate who knows no one
    '''now verifying candidate'''
    for i in range(0, n):
        if i != candidate and (knows(candidate,i) or not knows(i, candidate)) :
            return -1
    return candidate

# math expression recursion?