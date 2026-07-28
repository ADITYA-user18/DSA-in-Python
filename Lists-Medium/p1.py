arr = [1,2,2,2,5]
target = 2

i = 0
while i<len(arr):
    if arr[i]==target:
        print(i)
        break

    i+=1
