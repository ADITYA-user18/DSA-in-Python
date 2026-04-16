class Solution(object):
    def findMaxAverage(self, nums, k):

        cur = 0
        maxi = 0

        for i in range(k):
            cur+=nums[i]

        div = cur/float(k)
        maxi = div
        

        for i in range(k,len(nums)):
            cur+=nums[i]-nums[i-k]

            new_div = cur / float(k)

            maxi = max(maxi,new_div)

        return maxi


            

        
        
