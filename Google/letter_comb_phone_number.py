''' letter combinations of a phone number

given a string containing digits from 2-9 inclusive, return all
possible letter combinations that the number could represent

ex: "23" ==> ['ad','ae',...'bd','be',...'cd','ce','cf']
'''

def letterCombo(phoneNumber):
    if '0' in phoneNumber:
        return []
    if '1' in phoneNumber:
        return []
    result = []
    if not phoneNumber:
        return result
    digitToChar = {
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
            return result.append(builder)
        for letter in digitToChar[phoneNumber[index]]:
            helper(index+1, builder + letter)
    helper(0, '')
    return result

print letterCombo('6786883633')