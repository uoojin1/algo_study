'''
Alice has a hand of cards, given as an array of integers.

Now she wants to rearrange the cards into groups so that each group is size W, and consists of W consecutive cards.

Return true if and only if she can.
'''
hand = [1,2,3,6,2,3,4,7,8]
print hand.sort()
W = 3
import collections
# Output: true
# Explanation: Alice's hand can be rearranged as [1,2,3],[2,3,4],[6,7,8].

def isNStraightHand(hand, W):
    # count = collections.Counter(hand)
    count = {}
    for card_number in hand:
        if card_number in count:
            count[card_number] += 1
        else:
            count[card_number] = 1
    while count:
        m = min(count)
        print 'm', m
        for k in range(m, m+W):
            if k not in count: return False
            if count[k] == 1:
                del count[k]
            else:
                count[k] -= 1
    return True

isNStraightHand(hand, W)