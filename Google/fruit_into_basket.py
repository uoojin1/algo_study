''' fruit into baskets

in a row of trees, the i-th tree produces fruit with type tree[i]

start at any tree of ur choice, then perform these steps

1. add one piece of fruit from this tree to your baskets, if you cannot, stop
2. move the next ree to the right of the current ree, if there is no tree to the right, stop

each basket can carry any quantity of fruit, but you want each basket to only carry
one type of fruit each.

what is the total amount of fruit u can collect?
'''

''' example
input: [0,1,2,2]
output: 3
'''

# this is actually just longest substring with at most 2 characters

def totalFruit(trees):
    if not trees:
        return 0
    i = 0
    j = 1
    while j < len(trees) and trees[j] == trees[i]:
        j += 1
    if j == len(trees):
        return j-i
    maxTotal = j-i+1
    k = j+1
    count = maxTotal
    print i , j
    while k < len(trees):
        while k < len(trees) and (trees[k] == trees[i] or trees[k] == trees[j]):
            count += 1
            k += 1
        if count > maxTotal:
            maxTotal = count
        i = j
        j = k-1
        k += 1
        count = j-i+1
    return maxTotal


print totalFruit([1,1])
