class Solution:
    def sortZeroOneTwo(self, nums):

        zero = 0
        one = 0 
        two  = 0


        for num in nums:
            if num==0:
                zero+=1

            elif num==1:
                one+=1

            else:
                two+=1


        index  = 0

        while zero:
            nums[index] = 0
            index+=1
            zero-=1

        while one:
            nums[index] = 1
            index+=1
            one-=1


        while two:
            nums[index] = 2
            index+=1
            two-=1


        return nums
    

       
            
        



       
