s1 =  '10.20.30'
s2 = '4.5.6'


s1A = list(s1.split('.'))
s2A = list(s2.split('.'))

for i in range(len(s1A)):
    s1A[i] = int(s1A[i])

for i in range(len(s2A)):
    s2A[i] = int(s2A[i])


if(sum(s1A)>=sum(s2A)):
    print(True)

else:
    print(False)
