class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):

        res = []

        maxi = max(candies)


        for i in range(len(candies)):
            if extraCandies+candies[i] >= maxi:
                res.append(True)

            else:
                res.append(False)



        return res

        
        
        
