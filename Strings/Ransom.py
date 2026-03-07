class Solution(object):
    def canConstruct(self, ransomNote, magazine):

        dict = {}

        for ch in magazine:
            if ch not in dict:
                dict[ch] = 1
            else:
                dict[ch]+=1


        for ch in ransomNote:
            if ch  not in dict or dict[ch]==0:
                return False
            dict[ch] -= 1

        return True



       


       
        