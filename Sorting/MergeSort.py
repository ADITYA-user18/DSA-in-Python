
class Sorting:
    def mergeSort(self,nums):
          if len(nums) <= 1:
            return nums
          mid = len(nums)//2

          left = self.mergeSort(nums[:mid])
          right = self.mergeSort(nums[mid:])


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



t1 = Sorting()
a =t1.mergeSort([5,4,3,21,1,2,5,6,9])

print(a)