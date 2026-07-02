class Solution(object):
    def findDisappearedNumbers(self, nums):

        s = set(nums)

        num = []

        for i in range(1,len(nums)+1):
            if i not in s:
                num.append(i)


        return num


        

        



       

    
           
      
