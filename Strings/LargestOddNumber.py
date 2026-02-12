class LargestOdd:
    def GetLargestODddNumber(self,s):
        n = len(s)-1

        for i in range(n,-1,-1):
            if int(s[i])%2 == 1:
                return s[:i+1].lstrip('0')
        
        return ''

       


a = LargestOdd()
b = a.GetLargestODddNumber("0214638")

print(b)