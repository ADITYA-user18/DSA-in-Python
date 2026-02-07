class LowerBound:
    def findLower(self,nums,lower):
        left = 0
        right = len(nums)

        while left < right:
            mid = (left+right)//2
            
            if nums[mid] < lower:
                left = mid+1
            else:
                right = mid
        return left

    
a = LowerBound()
b = a.findLower([1,1,2,4,5,6,6,7,8],3)
print(b)