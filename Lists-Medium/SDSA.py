class Solution:
    def majorityElement(self, nums):

        d = {}

        for i in range(len(nums)):
            if nums[i]  not in d:
                d[nums[i]]=1

            else:
                d[nums[i]]+=1


        for num in nums:
            if d[num]>len(nums)//2:
                return num
        
