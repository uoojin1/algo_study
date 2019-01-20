''' Find the difference

Given 2 strings s and t, which only consists of lowercase letters,
string t is generated by shuffling string s and adding 1 more letter
find which letter was added in t
'''

''' my solution
iterate through s, and count how many times each character appears in s
so basically keep a hashmap that acts as counter
iterate through t, and decrement the counter.
if count was 0 before decrementing, this was the added character
'''

def findDifference(s, t):
    counter = {}
    for c in s:
        if c in counter:
            counter[c] += 1
        else:
            counter[c] = 1
    for c in t:
        if c in counter:
            counter[c] -= 1
            if counter[c] == -1:
                return c
        else:
            return c
    return '!'

print findDifference('abefg', 'abcfge')