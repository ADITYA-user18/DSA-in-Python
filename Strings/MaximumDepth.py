class MaxDepth:
    def DepthMaxiMum(self,s):
        n = len(s)
        maxDepth = 0
        currentDepth = 0


        for i in range(n):
            if s[i] == '(':
                currentDepth+=1
                maxDepth = max(maxDepth,currentDepth)
            elif s[i] == ')':
                currentDepth-=1

        return maxDepth

    
a = MaxDepth()
b = a.DepthMaxiMum("(1+(2*3)+((8)/4))+1")
print(b)

