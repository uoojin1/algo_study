''' Trailing zeros.

given number N, count trailing zeros in N!

so if N = 5
N! ==> 120
thus 1 trailing zero
'''

'''
so lets think about N = 10

10! = 1 * 2 * 3 * 4 * 5 * 6 * 7 * 8 * 9 * 10
      
        2*1      2*2     2*3    2*2*2    2*5

so count the number of fives
'''

'''
we basically need to count how many times 2 and 5 occur in the factorial, because 2*5 = 10
25 and 125 have two fives, and 3 fives and so..

so the trick is to count the number of 5s, divide by 5, do it again, and again , and again
'''

def findTrailingZeros(n):
    count = 0
    while n >= 5:
        count += n/5
        n /= 5
    return count

print findTrailingZeros(125)

