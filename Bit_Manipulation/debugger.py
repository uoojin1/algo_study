''' Debugger

Explain what the following code does: (n & (n-1)) == 0
'''

'''
let n = 0b0001 == 1
then n-1 = 0b0000
thus n and n-1 = 0

let n = 0b0011 = 3
then n-1 = 0b0010 = 2
thus n and n-1 = 0010 = 2

let n = 10000
so n-1= 01111
thus n and n-1 = 0

let n = 11000
so n-1= 10111

so basically there can be only 1 bit of 1, so 000010000 ==> 000001111
this basically means the number is a power of 2
'''