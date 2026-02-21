class MaxSubArray:
    def MaxiMumSubArray(self,nums,target):
        n = len(nums)
        maxi = 0

        for i in range(0,n):
            current_sum = 0
            for j in range(i,n):
                current_sum+=nums[j]

                if current_sum == target:
                    maxi =max(maxi,j-i+1)

        return maxi
    
a = MaxSubArray()
b = a.MaxiMumSubArray([1,2,3,1,1,1,1,4,2,3],6)
print(b)
            

