class Solution(object):
    def longestConsecutive(self, nums):

        if len(nums)==0:
            return 0

        sort = sorted(nums)
        current = 1
        maxi = 1


        for i in range(len(nums)-1):

            if sort[i]==sort[i+1]:
                continue

            elif sort[i+1]-sort[i]==1:
                current+=1

            else:
                maxi = max(maxi,current)
                current = 1


        return max(current,maxi)






           
        
        
