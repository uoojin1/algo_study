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

def recursiveMultiply(n1, n2):
    loopMax = min(n1, n2)
    largerNumber = max(n1, n2)
    def helper(a, counter, n):
        print 'a, counter, n', a, counter, n
        if counter == loopMax:
            return a
        return helper(a + n, counter + 1, n)
    return helper(0, 0, largerNumber)


print recursiveMultiply(15,13)
