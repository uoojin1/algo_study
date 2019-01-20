''' Recursive multiply
multiply 2 integers without * or / operator using recursive function

you can use addition, subtraction, and bit shifting, but you should minimize the number
of those operations
'''

''' example
5 x 3
== 5 + 5 + 5

-- probably looping with count = smaller number
'''

# def recursiveMultiply(n1, n2):
#     loopMax = min(n1, n2)
#     largerNumber = max(n1, n2)
#     def helper(a, counter, n):
#         print 'a, counter, n', a, counter, n
#         if counter == loopMax:
#             return a
#         return helper(a + n, counter + 1, n)
#     return helper(0, 0, largerNumber)


# print recursiveMultiply(15,13)

''' shifting?
so continuously add << 1 (times 2 ed)
'''

def shifting(n1, n2):
    maxShift = min(n1, n2)
    multVal = max(n1,n2)
    total = 0
    shifted = 0
    def helper(shiftCount, val):
        if shiftCount > maxShift:
            shifted = shiftCount
            return val
        return helper(shiftCount << 1, val << 1)
    total = helper(1, multVal)
    def helper2(shiftCount, val):
        print 'shift count vs max shift', shiftCount, maxShift
        if shiftCount <= maxShift:
            return val
        return helper2(shiftCount-1, val-multVal)
    return helper2(shifted, total)

print shifting(5,3)