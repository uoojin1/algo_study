''' Kth Largest Element in Array

find kth largest element in unsorted array

input: [3,2,1,5,6,4] and k = 2
we want to return 5
'''
import heapq

'''
we are using heap = thus we are using up more memory
compared to when we are sorting in memory O(1)
thus it is a trade off between memory and time
'''
# trivial way to solving this would be sorting
def findKthLargest(nums, k):
    # return sorted(nums)[len(nums)-k] (trivial)
    minHeap = []
    for num in nums:
        if len(minHeap) < k:
            heapq.heappush(minHeap, num)
        else:
            if num > minHeap[0]:
                minHeap[0] = num
                heapq.heapify(minHeap)
    return minHeap[0]

print findKthLargest([2,1,5,5,2,3,6,3,1], 3)