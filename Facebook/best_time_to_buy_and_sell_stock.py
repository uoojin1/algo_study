''' best time to buy and sell stock

say you have an array for which the ith element is the price of a given stock on day i

if you were only permitted to complete at most one transaction, buy one and sell one share
design an algorithm to find the maximum profit

* you cannot sell stock before you buy one

ex) [7,1,5,3,6,4]
output: 5 b/c you can buy at 1 and sell at 6 == 5

'''

def maxProfit(numbers):
    if not numbers:
        return None
    maxProfit = 0
    minPrice = numbers[0]
    for number in numbers:
        if number < minPrice:
            minPrice = number
        else:
            maxProfit = max(maxProfit, number - minPrice)
    return maxProfit

print maxProfit([1,3,2,4,5,8,2,3,1,6,8,19])
print maxProfit([1,2])