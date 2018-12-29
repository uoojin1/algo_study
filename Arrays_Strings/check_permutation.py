# given two strings, write a method to decide if one is a permutation of other
# (ex) "dog" <-> "god" and "dog   " ! <-> "god"


# def isPermutation(str1, str2):
#     if len(str1) != len(str2):
#         return False
#     # assuming these are ASCII strings, I will just use a fixed size array
#     checker = [0] * 128
#     for char in str1:
#         checker[ord(char)] += 1
#     for char in str2:
#         checker[ord(char)] -= 1
#     for val in checker:
#         if val != 0:
#             return False
#         else:
#             return True
#     return False
 
# print(isPermutation("azb  cx", "cba xz"))

# or a sorting solution

def isPermutation2(str1, str2):
    if len(str1) != len(str2):
        return False
    if sorted(str1) != sorted(str2):
        return False
    else:
        return True

print(isPermutation2("abcd", "abcd"))