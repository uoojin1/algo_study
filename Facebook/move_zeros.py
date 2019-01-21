''' move zeros

input: [0,1,0,3,12]
output: [1,3,12,0,0]

1. do this in place, w/o making a copy of the array
2. minimize the number of operations
'''

'''
[0, 1, 0, 3, 12]
       ^
so basically have a pointer that points to where I should put the next non zero element to
after iterating through the entire array, I should have all the non zero numbers put to the
left side of the array. and the index should point at the start index of 0s to the right
'''

def moveZeros(nums):
    index = 0
    for num in nums:
        if num != 0:
            nums[index] = num
            index += 1
    for i in range(index, len(nums)):
        nums[i] = 0
    return nums

print moveZeros([0,1,0,3,12,0,5,2,1,70,0,0,3,0,2,1,5])