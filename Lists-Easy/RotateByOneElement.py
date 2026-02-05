class Rotate:
    def ArrayRotation(self,nums):
        n = len(nums)
        d = nums[0]
        for i in range(1,n):
            nums[i-1] = nums[i]
        nums[n-1] = d
        return nums
a = Rotate()
b = a.ArrayRotation([1,2,3,4,5,6])

print(b)