''' hamming distance

the hamming distance between two integers is the number of positions at which the
corresponding bits are different

given two integers x and y, calculate the hamming distance

ex)
1: 0 0 0 1
4: 0 1 0 0
hamming diff is 2 (bits are different there)
'''

def hammingDistance(x, y):
    count = 0
    while y > 0 or x > 0:
        if (y & 1) ^ (x & 1) == 1:
            count += 1
        y /= 2
        x /= 2
    return count


print hammingDistance(3,4)