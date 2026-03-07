class Solution(object):
    def lengthOfLastWord(self, s):

        str_to_list = s.split()

        return len(str_to_list[-1])


        
        