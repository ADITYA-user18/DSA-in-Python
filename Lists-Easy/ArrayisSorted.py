class Sort:
    def IsSorted(self,nums):
        n = len(nums)
        count = 0

        if len(nums)==0:
            return False

        for i in range(0,len(nums)-1):
            if nums[i]>nums[i+1]:
                count+=1

        if count > 1:
                return False
        else:
                return True
            


a = Sort()
b = a.IsSorted([1,2,3])

print(b)