''' First Bad Version

u r a product manager
unfortunately, the latest version of your product fails the quality check.
all the versions after a bad version are also bad.
suppose you have n versions [1,2, ... n] and you want to find out the first bad one
you are given an API bool isBadVersion(version) which will return whethere version is bad

implement a function to find the first bad version.
you should minimize the number of calls to the API
'''

''' basically going to use binary search
1. choose the middle element
2. if that element is bad, repeat step one with left half of the array
2.1 else, repeat with right half
keep the index reference
'''

def isBadVersion(version):
    print 'API called!'
    if version == 1:
        return True
    else:
        return False

def recursivefirstBadVersion(nums):
    index = len(nums)/2
    
    def helper(ref, nums):
        print nums
        if len(nums) == 1:
            return ref
        if isBadVersion(nums[len(nums)/2]) and not isBadVersion(nums[len(nums)/2-1]):
            return ref + len(nums)/2
        if isBadVersion(nums[len(nums)/2]):
            return helper(ref, nums[:len(nums)/2])
        else:
            return helper(ref + len(nums)/2 + 1, nums[len(nums)/2+1:])
    return helper(0, nums)

print recursivefirstBadVersion([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1])

def iterativeSolution(nums):
    left = 1
    right = len(nums) - 1
    while left < right:
        middle = left + (right - left)/2
        if isBadVersion(nums[middle]):
            right = middle
        else:
            left = middle + 1
    return left

print iterativeSolution([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1])