''' Plus One

given an integer array, add one to it

[1, 0, 2] ==> [1, 0, 3]
'''

''' my solution
1. iterate from the back of the list
2. if not 9, add one and break loop
3. if 9, make zero and continue
4. if last iteration (first element in list) == 9, make zero and prepend 1 to the beginning
'''

def plusOne(numbers):
    length = len(numbers)
    i = length - 1
    while i >= 0:
        print 'i: ', i
        if numbers[i] == 9:
            numbers[i] = 0
            if i == 0:
                numbers.insert(0, 1)
        else:
            numbers[i] += 1
            break;
        i -= 1
    return numbers


print plusOne([9,9,9,9,9,9])