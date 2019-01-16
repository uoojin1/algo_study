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

def powerSet(numbers): # numbers == [1, 2, 3]
    if not numbers:
        return [numbers]
    elif len(numbers) == 1:
        return [[], numbers] # [[], [1]]
    else:
        rest = powerSet(numbers[1:])
        alist = []
        for item in rest:
            alist.append([numbers[0]]+item)
        return rest + alist
print powerSet([1,2,3])