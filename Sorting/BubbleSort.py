class Sort:
    def BubbleSort(self,nums):
        for i in range(0,len(nums)-1):
            for j in range(i+1,len(nums)):
                if nums[i]>nums[j]:
                    nums[i],nums[j] = nums[j],nums[i]
        return nums
a = Sort()
b = a.BubbleSort([1,5,28,53,5,26,5,85,2,1,2])

print(b)