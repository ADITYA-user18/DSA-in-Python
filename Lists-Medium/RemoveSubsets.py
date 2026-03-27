class Solution(object):
    def maximumUniqueSubarray(self, nums):

        left = 0
        seen = set()
        curr_sum = 0
        maxi = 0


        for right in range(len(nums)):
            while nums[right] in seen:
                seen.remove(nums[left])
                curr_sum-= nums[left]
                left+=1
            seen.add(nums[right])
            curr_sum += nums[right]

            maxi = max(maxi,curr_sum)

        return max
        
        


        
