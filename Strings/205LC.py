class Solution(object):
    def isIsomorphic(self, s, t):

        d1 =  {}
        d2 = {}

        for c1,c2 in zip(s,t):
            if c1 in d1 and d1[c1]!=c2:
                return False

            if c2 in d2 and d2[c2]!=c1:
                return False


            d1[c1] = c2
            d2[c2] = c1

        return True


        










        
       
        
