class Solution(object):
    def duplicateZeros(self, arr):


       original_length = len(arr)
       res = []

       for i in range(len(arr)):

        if arr[i]!=0:
            res.append(arr[i])

        elif arr[i]==0:
            res.append(0)
            res.append(0)


       for i in range(original_length):
        arr[i]=res[i]

       return arr


       
        
