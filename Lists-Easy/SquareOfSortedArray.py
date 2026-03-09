class Solution(object):
    def sortedSquares(self, nums):

        n = len(nums)

        res = []

        for i in range(n):
           res.append(nums[i]*nums[i])

        return sorted(res)
        
        