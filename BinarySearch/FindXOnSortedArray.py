class BinarySearch:
    def TargetFinder(self,nums,target):
        left = 0
        right = len(nums)-1

        for i in range(0,len(nums)):
            mid = (left+right)//2

            if target == nums[mid]:
                return mid
            
            if nums[mid]<target:
                left = mid+1

            elif nums[mid]>target:
                right = mid-1
        return f"No Target Found"
        

a = BinarySearch()
b = a.TargetFinder([2,3,4,5,6,7,8,9],6)
print(b)