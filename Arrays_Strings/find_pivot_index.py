'''
Given an array of integers nums, write a method that returns the "pivot" index of this array.

Input: 
nums = [1, 7, 3, 6, 5, 6]
Output: 3
Explanation: 
The sum of the numbers to the left of index 3 (nums[3] = 6) is equal to the sum of numbers to the right of index 3.
Also, 3 is the first index where this occurs.
'''
#       1  8  11 17 22 28
nums = [1, 7, 3, 6, 5, 6]
#       28 27 20 17 11 6
def pivotIndex(nums):
    