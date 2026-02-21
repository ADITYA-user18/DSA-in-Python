class MaxSubArray:
    def MaxiMumSubArray(self,nums,target):
        n = len(nums)
        maxi = 0

        for i in range(0,n):
            current_sum = 0
            for j in range(i,n):
                current_sum+=nums[j]

                if current_sum == target:
                    maxi = max(maxi,j-i+1)

        return maxi
    
a = MaxSubArray()
b = a.MaxiMumSubArray([6, -2, 2, -8, 1, 7, 4, -10],0)
print(b)
            

