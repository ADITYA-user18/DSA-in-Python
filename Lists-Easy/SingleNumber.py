class Solution(object):
    def singleNumber(self, nums):
        dict  = {}


        for i in range(0,len(nums)):
            if nums[i] not in dict:
                dict[nums[i]] = 1
            else:
                dict[nums[i]] += 1


        for key in dict:
            if dict[key] == 1:
                return key


        
        