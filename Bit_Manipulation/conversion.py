''' Conversion

Determine the number of bits you would need to flip
integer A to B

ex) 
29 == 11101
15 == 01111

output = 2
'''

''' Solution

so I think you basically need to find where the two bits are different
and you can do this by looking at 1 bit pair at a time and 
doing XOR operation. so that only when 1 bit is 1 and the other is 0,
the value would be 1 ==> meaning I found a 'difference'!
'''

def numberOfBitsToFlip(n1, n2):
    # i can get the first bit by and-ing with 1
    # so 11101 & 1 = 1

    # or i could just get a total XOR from the beginning
    xored = n1 ^ n2
    count = 0
    while xored > 0:
        count += xored & 1
        xored >>= 1
    return count
print numberOfBitsToFlip(0b101000, 0b111110)