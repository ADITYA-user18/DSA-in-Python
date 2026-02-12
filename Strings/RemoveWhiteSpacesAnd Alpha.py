class SpaceRemover:
    def removeWhiteSpaces(self,s):
        res = []
        seen = {'0','1','2','3','4','5','6','7','8','9','-','+'}

        for i in range(0,len(s)):
            if s[i] == ' ':
                continue
            if s[i] in seen:
                res.append(s[i])


        return "".join(res)
            

a = SpaceRemover()
b = a.removeWhiteSpaces('   Aditya -1382004     ')
print(b)