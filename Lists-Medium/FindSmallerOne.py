class Solution(object):
    def smallerNumbersThanCurrent(self, nums):

        sorter = sorted(nums)

        rank = {}

        for i in range(len(sorter)):
            if sorter[i] not in rank:
                rank[sorter[i]] = i
            
        result = []

        for num in nums:
            result.append(rank[num]) 


        return result



        
