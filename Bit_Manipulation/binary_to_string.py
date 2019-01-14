''' Binary to String

given a real number between 0 and 1 (eg 0.72)
print the binary representation.
If the number cannot be represented accurately in binary with at most 32 characters print "ERROR"
'''

'''
so if in decimal, the number was 0.72,
it's binary representation will be 0.xxxxxxxx

left shifting in binary is like multiplying the decimal by 2

so if 1.44 = x.xxxxxx
1 = x
'''

def binaryToString(decimalNumber):
    if decimalNumber < 0 or decimalNumber >= 1:
        return False
    binaryRepresentation = '0b0.'
    while decimalNumber > 0:
        print decimalNumber
        decimalNumber *= 2
        if len(binaryRepresentation) > 320:
            return "ERROR"
        if decimalNumber >= 1:
            binaryRepresentation += "1"
            decimalNumber -= 1
        else:
            binaryRepresentation += "0"
    return binaryRepresentation

print binaryToString(0.5)