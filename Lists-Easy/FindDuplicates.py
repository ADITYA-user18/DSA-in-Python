class Solution(object):
    def findDuplicate(self, nums):
       dicter = {}

       for i in range(len(nums)):
         if nums[i] not in dicter:
            dicter[nums[i]]=1
         else:
            dicter[nums[i]]+=1


       for num in dicter:
            if dicter[num] > 1:
                return num
