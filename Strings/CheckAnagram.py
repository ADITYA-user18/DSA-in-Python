class AnagramChecker:
    def CheckStringAnagram(self,x,y):

        if len(x) != len(y):
            return False
        
        freq = {}

        for ch in x:
            if ch not in freq:
                freq[ch] = 1
            else:
                freq[ch] +=1


        for ch in y:
            if ch not in freq:
                return False
            else:
                freq[ch]-=1
                del freq[ch]

        return len(freq)==0
    

a = AnagramChecker()
b = a.CheckStringAnagram('CAT','TAC')
print(b)
        


       
        
        


        
        