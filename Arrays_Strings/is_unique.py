# Is Unique: Implement an algorithm to determine 
# if a string has all unique characters. 
# What if you cannot use additional data structures?

## solution #############

# first, ask if the string is an ASCII string or a Unicode String
# Ascii = 7 bits, Unicode = 16 bits

# assuming the string is ASCII, we can basically count each character with a fixed size array

# def isUniqueChars(str):
#     if len(str) > 256:
#         return False
#     else:
#         checker = [0] * 256
#         for character in str:
#             if checker[ord(character)] == 0:
#                 checker[ord(character)] = 1
#             else:
#                 return False
#         return True

# print(isUniqueChars("abcdefgg"))

# if we assume the string will be only lowercase alphabets, there's only 26 possible characters
# thus the datastructure can just be 26 bits (int) instead of 256

# def isUniqueChars(str):
#     checker = [0] * 26
#     for character in str:
#         if checker[ord(character) - ord('a')] == 0:
#             checker[ord(character) - ord('a')] = 1
#         else:
#             return False
#     return True

# print(isUniqueChars("abcdefg"))

# or use bit vector

def isUniqueChars(str):
    checker = 0
    for character in str:
        val = ord(character) - ord('a')
        if (checker & (1 << val)) > 0:
            return False
        else:
            checker |= (1 << val)
    return True

print(isUniqueChars("abcdhefhg"))



#########################



# using a hashmap

# random_string = "abcndexfgh"
# char_set = {}
# found = 0

# for char in random_string:
#     if char in char_set:
#         found = 1
#     else:
#         char_set[char] = 1
# print(found)

# not using any datastructure

# random_string = "abcndedbbbbxfgh"
# found = 0

# counting_sort_array = [0] * 256

# for character in random_string:
#     counting_sort_array[ord(character)] = counting_sort_array[ord(character)]+1
# sorted_string = ''
# for index, value in enumerate(counting_sort_array):
#     for i in range(value):
#         sorted_string += chr(index)
# print(sorted_string)