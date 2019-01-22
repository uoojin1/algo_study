''' Best time to buy and sell stock 2

design an algorithm to find the maximum profit.
you may complete as many transactions as you like

ex.
input: [7,1,5,3,6,4]
output: 7
'''

''' so basically I think you want to buy when the current stock
that I'm on is less costly than the next one.

so im kind of buying and selling right away, each time I see
a increase, I just sell.
'''

def maxProfit(prices):
    if not prices:
        return 0
    profit = 0
    for i in range(0, len(prices)-1):
        if prices[i] < prices[i+1]:
            profit += prices[i+1] - prices[i]
    return profit

print maxProfit([7,1,5,3,6,4])