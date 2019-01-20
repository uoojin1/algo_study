''' a magic index in array A[] is index such that A[index] = index
from a sorted array of distinct integers, find magic index

A = [-2,-1,1,4,6]
index = 2
'''

''' we can use a binary search here

ex)
[-2,-1,1,4,6]
       ^
'''

def findMagicIndex(numbers):
    if not numbers:
        return None
    def helper(reference, numbers):
        if not numbers:
            return
        midIndex = len(numbers)/2
        print 'numbers: ', numbers
        print 'val vs middleIndex: ', numbers[midIndex], midIndex + reference
        if numbers[midIndex] == midIndex + reference:
            return reference + midIndex
        elif numbers[midIndex] < midIndex + reference:
            return helper(reference + midIndex + 1, numbers[midIndex+1:])
        else:
            return helper(reference, numbers[:midIndex])
    return helper(0, numbers)

print findMagicIndex([-2,-1,0,1,2,5,6,7])