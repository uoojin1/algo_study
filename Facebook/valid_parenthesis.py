''' valid parenthesis

given a string containing just the charaters '{}', '[]', '()'
determine if the input string is valid

input string is valid if
1. open brackets must be closed byb the same type of brackets
2. open brackets must be cloed in the correct order

note that empty string is also considered valid

ex) "()" ==> return true
"(){}[]" ==> return true
'''

def isValidParenthesis(s):
    if not s:
        return False
    if len(s) == 0:
        return True
    def findPair(c):
        if c == ']':
            return '['
        if c == '}':
            return '{'
        if c == ')':
            return '('
    openingParenthesis = []
    for c in s:
        print openingParenthesis
        if c == '{' or c == '[' or c == '(':
            openingParenthesis.append(c)
        else:
            if not openingParenthesis:
                return False
            popped = openingParenthesis.pop()
            if popped != findPair(c):
                return False
    if len(openingParenthesis) > 0:
        return False
    return True

print isValidParenthesis("{([])}(){[)]}")