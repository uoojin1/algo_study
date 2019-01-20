''' longest increasing subsequence

Input: [10,9,2,5,3,7,101,18]
Output: 4 
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4. 
'''

''' solution. probably use dynamib programming
basically starting from the back, I would ask wat's the longest substring until now

[]
'''

''' using dynamic programming...

what is the longest subsequence upto and including nums[i]??
'''

def lengthOfLongestIncreasingSubsequence(numbers):
    if not numbers:
        return 0
    res = [0]*len(numbers)
    res[0] = 1
    for i in range(1, len(numberes)):
        for j in range(i):
            if numbers[j] < numbers[i]:
                


lengthOfLongestIncreasingSubsequence([1,2,3,4,5,6])