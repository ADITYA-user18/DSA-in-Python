class Sort:
    def InsertionSort(self,nums):

        n = len(nums)
        for i in range(1,len(nums)):
            key = nums[i]
            j = i-1

            while j>=0 and nums[j]>key:
                nums[j+1] = nums[j]
                j-=1

            nums[j+1] = key

        return nums
    
a = Sort()
b = a.InsertionSort([12,88,2,25,5,2,5,23,2,58,])

print(b)