''' majority element

find element that appears more than half of the times
[3,2,3] = 3
'''

def majorityElement(numbers):
    counter = {}
    if not numbers:
        return None
    if len(numbers) == 1:
        return numbers[0]
    for number in numbers:
        if number in counter:
            counter[number] += 1
            if counter[number] >= len(numbers)/2:
                return number
        else:
            counter[number] = 1
    return None

print majorityElement([])