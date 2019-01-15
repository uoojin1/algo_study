# def quicksort(input):
#     if not input:
#         return []
#     pivot = input[0]
#     left = [x for x in input if x < pivot]
#     middle = [x for x in input if x == pivot]
#     right = [x for x in input if x > pivot]
#     return quicksort(left) + middle + quicksort(right)

# print quicksort([2,1,5,4,3,6,2,1])

def quicksort(input):
    if not input:
        return []
    if len(input) == 1:
        return input
    if len(input) == 2:
        if input[0] > input[1]:
            return [input[1], input[0]]
        else:
            return input
    pivot = input[0]
    temp = input[len(input)/2]
    input[len(input)/2] = pivot
    input[0] = temp
    # basically swapping the first element with middle element
    print input
    left = 0
    right = len(input)-1
    # initializing pointers
    '''7 3 4 4 5 6 3'''
    while left < right:
        while input[left] <= pivot:
            left += 1
        while input[right] > pivot:
            right -= 1
        temp = input[left]
        input[left] = input[right]
        input[right] = temp
        left += 1
        right -= 1
    
    return quicksort(input[:len(input)/2]) + [pivot] + quicksort(input[len(input)/2:])

print quicksort([3,4,5,2,1,9,5,7,8,1])

print sorted([4,1,7,5,2,7,1,4,6,8,9,4,5,1,3,6,1])