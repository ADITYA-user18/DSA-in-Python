class Solution(object):
    def sortColors(self, nums):
         if len(nums) <= 1:
            return nums
         mid = len(nums)//2

         left = self.sortColors(nums[:mid])
         right = self.sortColors(nums[mid:])


         i = j = k = 0

         while i < len(left) and j < len(right):
            if left[i]<=right[j]:
                nums[k] = left[i]
                i+=1
            else:
                nums[k] = right[j]
                j+=1
            k+=1

        
         while i<len(left):
            nums[k] = left[i]
            i+=1
            k+=1

         while j<len(right):
            nums[k] = right[j]
            j+=1
            k+=1

         return nums  


        
           



      
        