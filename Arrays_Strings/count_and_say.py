'''
1.     1
2.     11
3.     21
4.     1211
5.     111221

print out the n th string for given n
'''
class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        string = '1'
        for _ in range(n-1):
            letter, temp, count = string[0], '', 0
            for l in string:
                if letter == l:
                    count += 1
                else:
                    temp += str(count)+letter
                    letter = l
                    count = 1
            temp += str(count)+letter
            string = temp
        return string