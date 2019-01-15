''' Pairwise Swap

Write a program to swap odd and even bits in an integer with as few
instructions as possible

ex. bit 0 and bit 1 are swapped, bit 2 and bit 3 are swapped and so on

ex. 1010101010
==> 0101010101

ex. 11110000
==> 11110000

this can be done with masking and shifting

odd_mask = 10101010 == 0xaa
even_mask = 01010101 == 0x55
'''

def pairwiseSwap(n1):
    odd_mask = 0xaaaa
    even_mask = 0x5555
    return ((n1 & odd_mask) >> 1) | ((n1 & even_mask) << 1)

print bin(pairwiseSwap(0b11110101))