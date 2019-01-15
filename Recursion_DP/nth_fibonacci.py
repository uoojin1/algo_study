''' N th fibonacci

fibonacci sequence is this

1 1 2 3 5 8 13 ...

so each term is the summation of n-1 term and n-2 term
'''

# recursive solution
# def fibonacci(i):
#     if i == 0:
#         return 0
#     if i == 1:
#         return 1
#     return fibonacci(i-1) + fibonacci(i-2)

# print fibonacci(35)

''' runtime?

the runtime of the recursive solution is 2^n, becuase first of all draw a tree
each node has 2 children. so approximately
1
2
4
8
so the number of nodes = 1+2+4+8+...+2^n
thus O(2^n)
'''

''' However, there are a lot of duplicated work.
for example, fib(2) is calculated like 3 times, and we don't
need to do this.
thus, we should just memo the value of fib(2) and refer to it
'''

# def fibonacciHelper(i, memo):
#     if i == 0:
#         return 0
#     if i == 1:
#         return 1
#     if i in memo:
#         return memo[i]
#     memo[i] = fibonacciHelper(i-1, memo) + fibonacciHelper(i-2, memo)
#     return memo[i]

# def fibonacci(i):
#     memo = {}
#     return fibonacciHelper(i, memo)

# print fibonacci(40)

# def fibo(i):
#     memo = {}
#     def fiboHelper(i):
#         if i == 0:
#             return 0
#         if i == 1:
#             return 1
#         if i in memo:
#             return memo[i]
#         memo[i] = fiboHelper(i-1) + fiboHelper(i-2)
#         return memo[i]
#     return fiboHelper(i)

# print fibo(600)

'''bottom up approach'''
def fibonacci(i):
    if i == 0:
        return 0
    if i == 1:
        return 1
    memo = {}
    memo[1] = 1
    memo[2] = 1
    for index in range(3,i+1):
        memo[index] = memo[index-1] + memo[index-2]
    return memo[i]

print fibonacci(6)