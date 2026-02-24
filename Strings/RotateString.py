class StringRotation:
    def RotateString(self,s):
        lister = list(s)
        left = 0
        right = len(s)-1

        while left < right:
            lister[left],lister[right] = lister[right],lister[left]
            left+=1
            right-=1

        return ''.join(lister)
    
a = StringRotation()
b = a.RotateString('Developer')
print(b)