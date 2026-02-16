class MaxConsecutive:
    def ArrayMaxiConsecutive(self,nums):
        n = len(nums)
        count = 1
        maxi = 1

        for i in range(1,n):
            if nums[i] == nums[i-1]:
                count+=1
                maxi=  max(maxi,count)
            else:
                count=1

        return maxi
    
a = MaxConsecutive()
b = a.ArrayMaxiConsecutive([1,2,5,2,1,2,2,2,1,4,7,2,2,3,1,1,1,1,1,1,1,1,1,1,1])
print(b)


        

        
    
