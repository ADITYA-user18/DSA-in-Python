def fact(n):
    if n<=1:
        return n
    
    return  n*fact(n-1)


for i in range(10):
    print(fact(i),end='  ')