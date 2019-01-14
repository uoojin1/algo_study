''' Flip Bit to Win

You have an integer and you can flip exactly one bit from a 0 to a 1
Write code to find the length of the longest sequence of 1s you could create

example) 1  1 0 1 1 1 0 1 1 1 1 0
            2 ^     3           ^
countZero =   1       
max = 0 update this if the left + right > current max value
when we see the second zero, replace what we had for left with current right

until we see first 0, we increment left

when we see first 0, set right pointer to the next index of left pointer

while rightptr != 0

ex2) 0 0 0 1 1 1 1 0 0 0 0 0 1 1 1 1 
     ^ 

total 1s on the left += 1
set the right pointer to the next index

while loop

if we see zero, we would put the left pointer there
leftCount = rightCount
'''

## doing it like a bit problem

'''
by shifting the binary number to right, it's like doing /= 2
if the leftmost bit is 1 === the number is odd, we increment the current 1 sequence by 1

1 1 1 0 0 0 1 1 1
'''

def flipBitToWin(decimalNumber):
    binaryNumber = int(bin(decimalNumber), 2)
    curr_count = 0
    prev_count = 0
    maximum = 0
    print binaryNumber
    print bin(decimalNumber)
    while binaryNumber > 0:
        if binaryNumber % 2 == 1:
            curr_count += 1
        else:
            local_count = curr_count + prev_count + 1
            if local_count > maximum:
                maximum = local_count
            prev_count = curr_count
            curr_count = 0
        binaryNumber = binaryNumber >> 1
    if curr_count + prev_count + 1 > maximum:
        maximum = curr_count + prev_count + 1
    
    print 'maximum is!!: ', maximum

flipBitToWin(1246)






# def flipBitToWin(decimalNumber):
#     binaryNumber = bin(decimalNumber)[2:] ## cuts off the 0b part
#     left, right, i, maximum = 0, 0, 0, 0

#     print 'len', len(binaryNumber)
#     print binaryNumber

#     while i < len(binaryNumber) and binaryNumber[i] != '0':
#         i += 1
#         left += 1
#     # we found the first zero
#     i += 1
#     while i < len(binaryNumber):
#         print 'here'
#         while i < len(binaryNumber) and binaryNumber[i] != '0':
#             right += 1
#             i += 1
#         # we saw the second zero
#         if left+right+1 > maximum:
#             maximum = left+right+1
#         left = right
#         right = 0
#         i += 1
#     return maximum


# print flipBitToWin(45)