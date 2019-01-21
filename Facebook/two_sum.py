''' Two sum

given an array of integers, return indices of the two numbers such that they add up to a specfic target

you may assume that each input would have exactly one solution, and you may not use the same
element twice
'''

def twoSum(nums, target):
    history = {}
    for i, num in enumerate(nums):
        if target - num in history:
            return [history[target-num], i]
        else:
            history[num] = i
    return None

print twoSum([2,7,11,15], 22)