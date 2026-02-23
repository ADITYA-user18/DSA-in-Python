class RotatedSortedArray:
    def SortedArrayRotated(self,nums,X):
        n = len(nums)
        left =0
        right = len(nums)-1

        while left <= right:
            mid = (left+right)//2

            if nums[mid]==X:
                return mid
            
            if nums[left] <= nums[mid]:

                if nums[left] <= X < nums[mid]:
                    right = mid-1
                else:
                    left = mid+1

            else:

                if nums[mid]< X <= nums[right]:
                    left = mid+1
                else:
                    right = mid-1
        return -1
    

a = RotatedSortedArray()
b = a.SortedArrayRotated([4,5,6,7,0,1,2],0)
print(b)
    
            


