class Solution(object):
    def firstUniqChar(self, s):

        dicter = {}

        for ch in s:
            if ch not in dicter:
                dicter[ch] = 1
            else:
                dicter[ch]  +=1  
            

        for i in range(len(s)):
          if dicter[s[i]] == 1:
            return i
        return -1
      
        