class Solution(object):
    def validPalindrome(self, s):

        l = 0
        r = len(s)-1


        while l < r:
            if s[l]!=s[r]:
                removed_left = s[l+1:r+1]
                removed_right = s[l:r]

                return removed_left == removed_left[::-1] or removed_right==removed_right[::-1]
            l+=1
            r-=1

        return True



            

       
        
