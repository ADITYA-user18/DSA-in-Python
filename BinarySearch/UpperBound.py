class UP:
    def UpperBound(self,nums,x):
        left = 0
        right = len(nums)

        while left < right:
            mid = (left + right)//2

            if nums[mid] <= x:
                left = mid + 1
            else:
                right = mid

        return left
    

a = UP()
b = a.UpperBound([1,2,3,4,5,5,6,7,8,9,10,10,11,12,13],11)
print(b)