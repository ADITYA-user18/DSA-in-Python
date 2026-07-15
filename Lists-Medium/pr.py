arr = [5,3,6,1,9]

i = 1

curr  = 0

maxi = 0


while i < len(arr):
    if arr[i-1]>arr[i]:
        curr +=  arr[i-1]+arr[i]

        maxi = max(maxi,curr)

        curr=0

    i+=1


print(maxi)

        


