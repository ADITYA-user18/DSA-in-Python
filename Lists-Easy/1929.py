class Solution(object):
    def getConcatenation(self, nums):

        n = len(nums)
        i = 0
        while i < n:
            nums.append(nums[i])
            i+=1


        return nums
