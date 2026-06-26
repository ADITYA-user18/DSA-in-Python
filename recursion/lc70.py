class Solution(object):
    def climbStairs(self, n):

        if n<=2:
            return n
        
        prevOne = 2
        prevTwo = 1


        for i in range(3,n+1):
            current = prevTwo+prevOne
            prevTwo = prevOne
            prevOne = current


        return current

            


        


     
        
