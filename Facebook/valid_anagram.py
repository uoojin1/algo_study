''' valid anagram

given 2 strings s and t, determine if t is an anagram of s

ex) s = "anagram", t = "nagaram"
output == true
'''

# def isValidAnagram(s, t):
#     if len(s) != len(t):
#         return False
#     count = {}
#     for char in s:
#         if char in count:
#             count[char] += 1
#         else:
#             count[char] = 1
#     print count
#     for char in t:
#         if char in count:
#             count[char] -= 1
#             if count[char] < 0:
#                 return False
#         else:
#             return False
#     print count
#     for item in count:
#         if count[item] > 0:
#             return False
#     return True

def isValidAnagram(s, t):
    if len(s) != len(t):
        return False
    count = [0]*26 # number of alphabets
    for c in s:
        count[ord(c) - ord('a')] += 1
    for c in t:
        count[ord(c) - ord('a')] -= 1
    print count
    for num in count:
        if num > 0:
            return False
    return True

print isValidAnagram('gabcxe', 'abcefg')