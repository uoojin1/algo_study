''' contains duplicate

return true if there are no duplicate numbers in an array
else false
'''

def containsDuplicate(numberList):
    seen = set()
    for number in numberList:
        if number in seen:
            return True
        seen.add(number)
    return False

test_case = [1,2,3,4,5,6,7,8]

print containsDuplicate(test_case)