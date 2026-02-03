class Sort:
    def selectionSort(self,nums):
        n = len(nums)
        for i in range(0,n-1):
            min_Index  = i

            for j in range(i+1,n):
                if nums[j]<nums[min_Index]:
                    min_Index = j
                
                nums[min_Index],nums[i] = nums[i],nums[min_Index]

        return nums


a = Sort()
b = a.selectionSort([1,2,8,74,96,6,2,5])
print(b)