class Solution(object):
    def strStr(self, haystack, needle):

        if needle=='':
            return -1

        
        for i in range(len(haystack)):
            if haystack[i:i+len(needle)]==needle:
                return i

        return -1

        

        


        
        
