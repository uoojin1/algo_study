''' climbing stairs

given integer n (steps of stairs)
how many ways can you climb it?
given that u can climb 1 stair or 2 stairs at a time
'''

def climbStairs(n):
    memo = {}
    def helper(n):
        if n == 0:
            return 0
        if n == 1:
            return 1
        if n == 2:
            return 2
        if n in memo:
            return memo[n]
        else:
            total = helper(n-1) + helper(n-2)
            memo[n] = total
            return total
    return helper(n)

def climbStairsNoMemo(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    if n == 2:
        return 2
    return climbStairsNoMemo(n-1) + climbStairsNoMemo(n-2)

print 'with memo: ', climbStairs(30)
# print 'no memo!',  climbStairsNoMemo(35)

def climeStairsBottomUp(n):
    memo = {}
    memo[0] = 1
    memo[1] = 1
    memo[2] = 2
    for i in range(2, n+1):
        memo[i] = memo[i-1] + memo[i-2]
    return memo[n]

print climeStairsBottomUp(30)