''' Triple Step

a child is running up a staircase with n steps and can hop either 1 step, 2steps
or 3 steps at a time. implement a method to count how many possible ways the
child can run up the stairs
'''

def tripleStep(n): # n == stair case height
    if n == 0:
        return 0
    if n == 1:
        return 1 # if he is at the first step, there's only 1 way
    if n == 2:
        return 2
    if n == 3:
        return 4
    return tripleStep(n-1) + tripleStep(n-2) + tripleStep(n-3)

# print tripleStep(30)

def tripleStepWithMemo(n):
    memo = {}
    def helper(n):
        if n == 0:
            return 0
        if n == 1:
            return 1
        if n == 2:
            return 2
        if n == 3:
            return 4
        if n in memo:
            return memo[n]
        memo[n] = helper(n-3) + helper(n-2) + helper(n-1)
        return memo[n]
    return helper(n)

print tripleStepWithMemo(2000)