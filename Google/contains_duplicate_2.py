''' Contains Duplicate 2

given an array of integers and an integer k, find out whether there are
2 distinct indices i and j in the array such that nums[i] == nums[j]
and the absolute difference between i and j at most k
'''

''' example

k = 3
arr = [1,2,3,1] == should re turn true

k = 1
arr = [1,2,1,1] == should return true
'''

# my solution
'''
# need to look at the history to see what things appeared when.
# would be nice to use hashmap with key as the number, value as the index

1. as iterating through array, we will build such hashmap
2. for each number, see if that number appeared before (check hashmap)
3. if it did, check if that number appeared within the given accepted time frame
3.1. if yes, return True
3.2. if no, update the value to the current index (b/c we want to keep the most up to date index)
4. if we didn't find one even after going through the array, return False
'''

def containsDuplicate(numbers, k):
    seen = {}
    for i, number in enumerate(numbers):
        if number in seen:
            if i - seen[number] <= k:
                return True
        seen[number] = i
    return False

print containsDuplicate([1,1], 1)