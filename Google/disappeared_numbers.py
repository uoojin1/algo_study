''' disappeared numbers in array

given an array of integers where 1 <= a[i] <= n (size of array)
some elements appear twice and others apepar once
find all the elements of [1,n] inclusive that do not appear in this array
'''

def disappearedNumbers(numbers):
    seen = set()
    missingNumbers = []
    for number in numbers:
        seen.add(number)
    for i in range (1,len(numbers)+1):
        if i not in seen:
            missingNumbers.append(i)
    return missingNumbers

# print disappearedNumbers([1,2,9,5,2,1,4,6,6,9])

''' O(1) space solution
1. basically mark the value at the right index by placing a negative sign
'''

def o1Solution(numbers):
    for i, value in enumerate(numbers):
        index = abs(numbers[i]) - 1
        numbers[index] = -1 * abs(numbers[index])
        # print numbers
    # print numbers
    missingNumbers = []

    for i in range(0, len(numbers)):
        if numbers[i] > 0:
            missingNumbers.append(i+1)
    return missingNumbers
    
print o1Solution([3,2,3,3])