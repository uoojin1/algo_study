''' Power Set

return all subsets of a set
'''

''' examplple

(1, 2, 3)

power set ==> [(1),(2),(3),(1,2),(1,3),(2,3),(1,2,3)]
'''

''' solution

so you can basically start from a empty list,
go through the numbers from left to right,
decide if you want to either add or ignore
'''

# def powerSet(numbers): # numbers == [1, 2, 3]
#     if not numbers:
#         return [numbers]
#     elif len(numbers) == 1:
#         return [[], numbers] # [[], [1]]
#     else:
#         rest = powerSet(numbers[1:])
#         # print rest
#         alist = []
#         for item in rest:
#             alist.append([numbers[0]]+item)
#         print 'rest', rest
#         print 'alist', alist
#         return rest + alist
# print powerSet([1,2,3])


# def powerSet(numberList):
#     if not numberList:
#         return [numberList]
#     if len(numberList) == 1:
#         return [[],[numberList[0]]]

#     rest = powerSet(numberList[1:]) # get the rest recursively
#     allList = []
#     print 'rest', rest
#     for item in rest:
#         allList.append([numberList[0]]+item)
#     return rest + allList

# print powerSet([1,2,3])

def powerSet(numbers):
    if not numbers:
        return [numbers]
    if len(numbers) == 1:
        return [[], [numbers[0]]]

    rest = powerSet(numbers[1:])

    currentValueAdded = []
    for item in rest:
        currentValueAdded.append([numbers[0]]+item)
    
    return currentValueAdded + rest

print powerSet([1,2,3])