''' Power Set
write a method to return all subsets of a set

so [1, 2]
reuslt = [[],[1],[2],[1,2]]
'''

def powerSet(numbers):
    if not numbers:
        return []
    def helper(numbers):
        if len(numbers) == 0:
            return [[]]
        if len(numbers) == 1:
            return [[], [numbers[0]]]
        rest = helper(numbers[1:])
        added = []
        for item in rest:
            added.append(item + [numbers[0]])
        return added + rest
    return helper(numbers)

print powerSet([1,2,3])