class IndexPosition:
    def IndexPositioner(self,nums,x):
        left = 0
        right = len(nums)-1

        while left < right:
            mid = (left+right)//2

            if nums[mid] < x:
                left = mid+1

            else:
                right = mid


        return left
    
a = IndexPosition()
b = a.IndexPositioner([1,2,3,4,5,6,7,9,10],8)
print(b)
