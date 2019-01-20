''' Triple Step

a child is running up a staircase with n steps and can hop either 1 step, 2 steps,
or 3 steps at a time. Implement a method to count how many possible ways the child
can run up the stairs
'''

''' basically a dynamic programming problem
basically to get to step, i, I could have came from i-1 or i-2 or i-3
thus, I need to add all of the ways i could have came to those steps
'''

# def tripleStep(n):
#     if not n or n <= 0:
#         return 0
#     if n == 1:
#         return 1
#     if n == 2:
#         return 2
#     if n == 3:
#         return 4
#     return tripleStep(n-1) + tripleStep(n-2) + tripleStep(n-3)

# print tripleStep(8)

def withMemo(n):
    if not n:
        return 0
    memo = {}
    def helper(n):
        if n == 0:
            return 0
        if n == 1:
            return 1
        if n == 2:
            return 3
        if n == 3:
            return 4
        if n in memo:
            return memo[n]
        memo[n] = helper(n-3) + helper(n-2) + helper(n-1)
        return memo[n]
    return helper(n)

print withMemo(2000)

# def tripleStepWithMemo(n):
#     if not n or n <= 0:
#         return 0
#     memo = {}
#     memo[1] = 1
#     memo[2] = 2
#     memo[3] = 4
#     for i in range(4, n+1):
#         memo[i] = memo[i-1] + memo[i-2] + memo[i-3]
#     return memo[n]

# print tripleStepWithMemo(8)