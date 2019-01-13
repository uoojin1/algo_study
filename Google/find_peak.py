''' Find Peak Element

[1,2,3,4,5,6,7,8,5]
return 7 (index of 8)
'''

# simple solution --> linear search from beginning , keep a current max

## better solution (binary search!)
''' Binary Search
if next element is less than the curr, at least one local maxima has to exist on the left side
if next element is greater or equal than the curr, at least one local maxima has to exist on the right side
thus, do this using binary search
'''

def findPeakElement(numbers):
    left = 0
    right = len(numbers)-1
    while left < right:
        print left, right
        midIndex = left + (right-left)/2
        if numbers[midIndex] < numbers[midIndex + 1]:
            left = midIndex + 1
        else:
            right = midIndex
    return left

print findPeakElement([1,2,3,6,7,6,7,8,3])