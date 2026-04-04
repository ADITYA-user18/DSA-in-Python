class Solution(object):
    def numJewelsInStones(self, jewels, stones):
       
       d = {}

       for stone in  stones:
        if stone not in d:
            d[stone] = 1
        else:
            d[stone]+=1

       count=0
       for ch in jewels:
            if ch in d:
                count+=d[ch]

       return count
        
