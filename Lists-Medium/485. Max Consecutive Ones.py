class Solution(object):
    def findMaxConsecutiveOnes(self, nums):

        count = 0

        i = 0 
        maxi = 0


        while i < len(nums):
            if nums[i]==1:
                count+=1
                maxi = max(count,maxi)

            else:
                count=0

            i+=1


        return maxi
       
