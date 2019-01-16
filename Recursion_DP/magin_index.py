''' Magic index

Magic index in an array A[0 ~ n-1] is defined to be an index such that
A[i] = i. Given a sorted array of distinct integers, write a method to find a magic index.
if one exists, in array A
'''

''' example
A = [-1, 0, 2, 4, 5, 7]
return 2

O(n)

O(n) ==> O(logn) or O(1)

binary search, we

A = [-1, 0, 1, 2, 5, 7, 9]
      0  1  2  3  4  5  6

      check if A[i] = i
      if A[i] < i at some i
      then, there is no way that the A[i] for indexes < i, to have A[index] = index

    A[i] == length 1:: [1] == index ==> return true
    if not A return false

'''

def magicIndex(A, ref):
    print 'A and ref', A, ref
    if not A:
        return -1
    index = len(A)/2
    print 'index: ', index
    if A[index] == index:
        return ref + index
    elif A[index] < index:
        return magicIndex(A[len(A)/2+1:], ref + len(A)/2)
    else:
        return magicIndex(A[:len(A)/2], ref)

print magicIndex([-5,-4,-3,2,4,7,8,9,10], 0)


''' Duplicate?

in the case duplicates I think the algo will fail
'''


example = [0, 0, 1, 2, 2, 3, 4, 5, 6]

