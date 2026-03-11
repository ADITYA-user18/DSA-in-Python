class Solution(object):
    def threeSum(self, nums):
        target = 0
        res = set()
        n = len(nums)
        for i in range(n):
             seen = set()
             for j in range(i+1,n):
                remain = target - (nums[i]+nums[j])
                if remain in seen:
                  result = tuple(sorted([nums[i],nums[j],remain]))
                  res.add(result)
                seen.add(nums[j])
        
        return list(res)
        
                


            
        