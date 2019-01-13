''' Backspace string compare

given two strings S and T, return if they are equal when both are typed into
empty text editors.

# means a backspace character

ex) S = 'ab#c', T = 'ad#c'
output: True
Explanation: both S and T = 'ac'

BUT CAN YOU SOLVE IT IN O(1) SPACE COMPLEXITY?
'''

def processString(string):
    stack = []
    for char in string:
        if char != '#':
            stack.append(char)
        elif char == '#' and stack:
            stack.pop()
    return stack

def backspaceCompare(S, T):
    sStack = processString(S)
    tStack = processString(T)
    # print sStack, tStack
    if sStack == tStack:
        return True
    else:
        return False

# print backspaceCompare('ab####ac', 'ad#c')

''' O(1) space solution
1. iterate through the string backwards
2. each time we see a backspace character, the next non backspace character should be skipped
3. if it isn't skipped, it is part of the answer
'''
import itertools

def betterBackspaceCompare(S, T):
    def processString(S):
        skip = 0
        for char in reversed(S):
            if char == '#':
                skip += 1
            elif skip > 0:
                skip -= 1
            else:
                yield char
    print processString(S)
    for char in processString(S):
        print char
    return all(x == y for x,y in itertools.izip_longest(processString(S), processString(T)))

print betterBackspaceCompare('ab#badbasdfcc#', 'ad#c')

# def betterBackspaceCompare(S, T):
#     # s_index = len(S) - 1
#     # t_index = len(T) - 1
#     def processString(S):
#         skip = 0
#         newString = []
#         for char in reversed(S):
#             if char == '#':
#                 skip += 1
#             elif skip > 0:
#                 skip -= 1
#             else:
#                 yield char
#         #         newString.append(char)
#         # return newString
#     return all(x == y for x,y in itertools.izip_longest(processString(S),processString(T))) #processString(S) == processString(T)

# print betterBackspaceCompare('ab#cc#', 'ad#c')

