'''
Given a string s, partition s such that every substring of the partition is a palindrome.

Return all possible palindrome partitioning of s.

Example:

Input: "aab"
Output:
[
  ["aa","b"],
  ["a","a","b"]
]
'''

def partition(s):
    ret = []
    for i in range(1, len(s)+1):
        '''
        s[:i] and s[i-1::-1] is basically flip of eachother
        after the if, we know that we found a section of array that is a palindrome
        '''
        if s[:i] == s[i-1::-1]:
            for rest in partition(s[i:]): 
                ret.append([s[:i]]+rest)
    if not ret:
        return [[]]
    return ret


