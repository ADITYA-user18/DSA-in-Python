class Solution(object):
    def dominantIndex(self, nums):
        first = 0
        second = 0
        index =-1


        for i in range(len(nums)):
            if nums[i]>first:
                second = first
                first = nums[i]
                index = i

            elif nums[i]>second and nums[i]!= first:
                second = nums[i]



        if first >= 2*second:
            return index
        else:
            return -1

        


       
        
        