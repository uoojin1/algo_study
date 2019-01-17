# def solutions(S, K):
#     noDashS = S.replace('-','')
#     sLength = len(noDashS)
#     remainder = sLength % K
#     print 'remainder', remainder
#     result = ''

#     for i in range(0,remainder):
#         result += noDashS[i]
#     result += '-'

#     count = 1
#     noDashS = noDashS[remainder:]

#     print noDashS
#     for i in range(0, len(noDashS)):
#         print i
#         if count == K+1:
#             result += '-'
#             count = 1
#         result += noDashS[i]
#         count += 1

#     print 'result', result

# solutions("abc-de-fghijkl-m",4)

'''
def solution(S, K):
    # write your code in Python 3.6
    if not S:
        return ''
    noDashS = S.replace('-','')
    sLength = len(noDashS)
    if sLength == 0:
        return ''
    if K > sLength:
        return ''
    remainder = sLength % K
    result = ''
    
    for i in range(0, remainder):
        result += noDashS[i]
    if remainder != 0:
        result += '-'
    
    count = 1
    noDashS = noDashS[remainder:]
    
    for i in range(0, len(noDashS)):
        if count == K+1:
            result += '-'
            count = 1
        result += noDashS[i]
        count += 1
    
    return result.upper()
    
'''

def solution(coupons):
    memo = {}
    answer = -1
    for i, coupon in enumerate(coupons):
        if coupon in memo: # we found another one and should calculate length
            needToBuy = i - memo[coupon] + 1
            if answer == -1:
                answer = needToBuy
            elif needToBuy < answer and answer != -1:
                answer = needToBuy
            memo[coupon] = i
        else:
            memo[coupon] = i
    return answer

print solution([3,6,1,9])
[5,3,4,2,3,4,5,7]

[]
[1]
[1,1,1,1,1,1,1]
[1,0,1,0,1,-1,0]
[1,2,3,4,5,6,7]
[1,2,3,4,5,6,7,8,1]
