arr = [2,1,5,1,3,2]
k = 3


curr = 0
maxi = 0
for i in range(k):
    curr+=arr[i]
    maxi = max(maxi,curr)


for i in range(k,len(arr)):
    curr = curr + arr[i] - arr[i-k]

    maxi = max(maxi,curr)


print(maxi)






    


    

