''' add binary

given 2 binary strings, return their sum (also a binary string)
The input strings are both non-empty and contains only characters 1 or 0

ex)

a = "11"
b = "1"

output == "100"
'''

def addBinary(a, b):
    # duration = max(len(a), len(b))
    answer = ''
    i = len(a) - 1
    j = len(b) - 1
    carry = 0
    while i >= 0 or j >= 0:
        total = carry
        if i >= 0:
            total += ord(a[i]) - ord('0')
        if j >= 0:
            total += ord(b[i]) - ord('0')
        carry = total/2
        answer = str(total%2) + answer 
        # print total % 2
        print chr(total%2)
        i -= 1
        j -= 1
    if carry == 1:
        answer = '1' + answer
    return answer

print addBinary("111","101")