'''
Assume you have a method isSubstring which checks if one word is a substring of another.

given 2 strings, str1 and str2, write code to check if s2 is a rotation of s1 using only one
call to isSubstring()

ex. "waterbottle" is a rotation of "erbottlewat"
'''

'''
str1 = 456789123
str2 = 123456789
'''

def isSubstring(str1, str2):
    return True if str1 in str2 else False

def isRotation(str1, str2):
    if len(str1) != len(str2):
        return False
    string_to_compare_to = str1 + str1
    return True if isSubstring(str2, string_to_compare_to) else False
'''
runtime depends on the isSubstring method, but is is generally O(len(str1) + len(str2))
so time complexity = O(n)
'''
print(isRotation("12345", "45123"))
