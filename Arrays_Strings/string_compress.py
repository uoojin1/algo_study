# Implement a method to perform basic string compression using the counts of repeated characters. 
# For example, the string aabcccccaaa would become a2blc5a3.

def compressor(str1):
    char_count = {}
    for char in str1:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    compressed_string = ''
    for char in char_count:
        compressed_string += char
        compressed_string += str(char_count[char])
    return compressed_string

print(compressor("aaaabbbbccdd"))