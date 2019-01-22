''' remove dups from sorted array

do not allocate extra space for another array, must do this by modifying the input array
in-place with O1 extra memory
'''

def removeDupsFromSortedArray(nums):
    if not nums:
        return 0
    if len(nums) == 1:
        return nums
    index = 0
    prevNumber = None
    
    for i in range(0, len(nums)):
        if nums[i] != prevNumber:
            nums[index] = nums[i]
            index += 1
        prevNumber = nums[i]

    return nums[:index]

print removeDupsFromSortedArray([1,1,1,2,2,2,3,3,4,4,5,6,6,7,7,7,7,7,7,8])