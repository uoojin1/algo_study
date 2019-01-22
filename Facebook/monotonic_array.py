''' monotonic array

array is monotonic if it is increasing or decreasing

return true if array A is monotonic

ex) [1,2,2,3], true

'''

def isMonotonic(nums):
    if not nums:
        return True
    if len(nums) == 1 or len(nums) == 2:
        return True
    isDecreasing = nums[1] < nums[0]

    prev = nums[0]

    for i in range(1, len(nums)):
        curr = nums[i]
        print curr
        if isDecreasing:
            if curr > prev:
                return False
        else:
            if curr < prev:
                return False
        prev = curr
    return True

x = [1,1,2,3,3,4,4,5,5,6,6,7,11]
print x[::-1]
print isMonotonic(x)
print isMonotonic(x[::-1])