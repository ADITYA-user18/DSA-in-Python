class Solution(object):
    def longestPalindrome(self, s):

        d = {}

        for i in range(len(s)):
            if s[i] not in d:
                d[s[i]] =1

            else:
                d[s[i]]+=1


        ans = 0
        odd= False

        for count in d.values():
            if count%2==0:
                ans+=count

            else:
                ans+=count-1
                odd = True

        
        if odd:
            ans+=1


        return ans
        
        
