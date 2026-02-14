class FirstOccurence:
    def OccurenceChecker(self,nums,x):
        n = len(nums)
        left =0
        right = len(nums)-1

        while left <= right:
            mid = (left+right)//2

            if nums[mid] < x:
                left = mid+1
            else:
                right = mid-1

        return left
    
a = FirstOccurence()
b = a.OccurenceChecker([1,2,2,2,2,3,4,5,5,6,7,8,9,10,11],2)
print(b)
            



