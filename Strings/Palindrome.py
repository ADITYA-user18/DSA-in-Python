class Solution(object):
    def isPalindrome(self, s):
        if len(s)== " ":
            return True

        alnum = ''
        
        for ch in s:
            if ch.isalnum():
                alnum += ch.lower()


        left = 0
        right = len(alnum)-1


        while left < right:
            if alnum[left]==alnum[right]:
                left+=1
                right-=1
                continue
            else:
                return False
        
        return True


                 


        
        