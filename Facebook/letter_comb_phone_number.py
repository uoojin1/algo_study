''' given phone number, print out its all possible letter combs
'''

def letterComb(phoneNumber):
    if '1' in phoneNumber or '0' in phoneNumber:
        return []
    combinations = []
    if not phoneNumber:
        return combinations
    mapping = {
        '2': 'abc',
        '3': 'def',
        '4': 'ghi',
        '5': 'jkl',
        '6': 'mno',
        '7': 'pqrs',
        '8': 'tuv',
        '9': 'wxyz'
    }

    def helper(index, builder):
        if index == len(phoneNumber):
            combinations.append(builder)
            return
        for c in mapping[phoneNumber[index]]:
            helper(index+1, builder + c)
    
    helper(0, '')
    return combinations

print letterComb('6476883633')
        