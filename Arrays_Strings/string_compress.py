# Implement a method to perform basic string compression using the counts of repeated characters. 
# For example, the string aabcccccaaa would become a2blc5a3.

# def compressor(str1):
#     char_count = {}
#     for char in str1:
#         if char in char_count:
#             char_count[char] += 1
#         else:
#             char_count[char] = 1
#     compressed_string = ''
#     for char in char_count:
#         compressed_string += char
#         compressed_string += str(char_count[char])
#     return compressed_string

# print(compressor("aaaabbbbccdd"))

# def stringCompressor(string):
#     char_count = 0
#     prev_char = None
#     output_string = ''
#     if len(string) > 0:
#         for char in string:
#             if char != prev_char:
#                 if prev_char != None:
#                     output_string += str(char_count)
#                 output_string += char
#                 char_count = 1
#             else:
#                 char_count += 1
#             prev_char = char
#         output_string += str(char_count)
#     if len(string) < len(output_string):
#         return string
#     else:
#         return output_string
# print(stringCompressor("abab"))

def stringCompressor(string):
    if len(string) < 3:
        return string
    compressed_string = ''
    current_char_count = 0
    for i in range(len(string) - 1): # to avoid indexing issue
        current_char_count += 1
        if string[i] != string[i+1]: # current char is different from next char
            compressed_string += string[i] + str(current_char_count)
            current_char_count = 0
    # think it as iterating through the last loop manually
    current_char_count += 1
    if string[len(string)-1] != None:
        compressed_string += string[len(string)-1] + str(current_char_count)
        current_char_count = 0
    return string if len(string) < len(compressed_string) else compressed_string

print(stringCompressor("aaccccccca"))