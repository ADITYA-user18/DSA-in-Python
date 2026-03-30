class Solution(object):
    def thirdMax(self, nums):

        first = second = third = -float('inf')


        for num in nums:
            if num > first:
                third = second
                second = first
                first = num
            elif num > second and num != first:
                third = second
                second = num
            
            elif num > third and num!=first and num != second:
                third = num

        
        if third not in nums:
            return first
        else:
            return third
        
        
