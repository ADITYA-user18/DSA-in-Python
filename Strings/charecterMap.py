class CharacterMapping:
    def mapCharecters(self,S,A):
        n = len(S)
        m = len(A)
        seen1 = []
        seen2 = []

        if n != m:
            return False

        for i in range(0,n):
            if S[i] not in seen1:
                seen1.append(S[i])

        for i in range(0,m):
            if A[i] not in seen2:
                seen2.append(A[i])

        a = 0
        b = 0

        while a < len(seen1) and b < len(seen2):
            print(f'{seen1[a]} => {seen2[b]}',end=' , ')
            a+=1
            b+=1

        return ''
    

a = CharacterMapping()
b = a.mapCharecters("foo","bar")
print(b)
            


            

