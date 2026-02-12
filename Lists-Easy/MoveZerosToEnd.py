class MoveZerosToEnd:
    def ZeroMoverToEnd(self,nums):
        k = 0

        for i in range(0,len(nums)):
            if nums[i] != 0:
                nums[i],nums[k] = nums[k],nums[i]
                k+=1

        return nums
    

a = MoveZerosToEnd()
b = a.ZeroMoverToEnd([1,2,4,5,0,1,5,9,6,0,3,5,0,1,2,0,2,0])
print(b)