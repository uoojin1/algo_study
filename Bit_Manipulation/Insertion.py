''' Insertion

given 
two 32-bit numbers N and M
and two bit positions i and j

write a method to insert M into N such that M starts at bit j and ends at i
you can assume that there are al least 5 bits between j and i
'''

''' example
input:  N = 10000000000, M = 10011, i=2 j=6
output: N = 10001001100
'''

#solution: need to decide how many shifts to apply to M :: << 1
'''
for example, if len(M) = 5 and i=2 j=6 (j-i+1) = 5
I would just shift by i

however if j=6 and i=1, this is longer than the length of M 
so I will need to shift by i + (how many bits is the given space larger than M)
== i + [(j-i+1) - len(M)]
'''

def insertion(N, M, i, j):
    # creating 2 masks for the left and right
    leftMask = ~0 << (j+1)
    rightMask = 1 << (i+1) - 1
    mask = leftMask | rightMask

    maskedN = N & mask
    shiftedM = M << i

    return maskedN | shiftedM

print insertion(0b1000000000, 0b11011, 2, 5)