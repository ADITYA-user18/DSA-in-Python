class Solution(object):
    def numOfSubarrays(self, arr, k, threshold):
        
        curr = 0
        count = 0


        for i in range(k):
            curr+=arr[i]

        first_avg = curr//k

        if first_avg >= threshold:
            count+=1
            

        for i in range(k,len(arr)):

            curr += arr[i]-arr[i-k]

            first_avg = curr//k

            if first_avg >= threshold:
                count+=1
                

        return count
        


            



        
