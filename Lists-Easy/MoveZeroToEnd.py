class ZerosToEnd:
    def Zeros(self,nums):
        i = 0
        for j in range(0,len(nums)):
            if nums[j]!=0:
                nums[i],nums[j] = nums[j],nums[i]
                i+=1

        return nums

a = ZerosToEnd()
b = a.Zeros([21,4,2,1,0,7,5,3,9,5,1,0])
print(b)
