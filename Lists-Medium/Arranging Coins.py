class Solution(object):
    def arrangeCoins(self, n):
        i = 1
        rows = 0

        while n >= i:
            n -= i
            i += 1
            rows += 1

        return rows
