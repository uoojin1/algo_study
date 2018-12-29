# given a string, check if palindrome permutation

# this basically means that it only has one odd char count at max

def isPalPerm(str):
    char_count = {}
    for char in str:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    odd_count = 0
    for char in char_count:
        if char_count[char] % 2 == 1:
            odd_count += 1
    if odd_count > 1:
        return False
    else:
        return True

print(isPalPerm('abcxcxcba'))