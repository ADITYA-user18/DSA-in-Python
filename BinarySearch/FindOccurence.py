class OccurenceFinder:
    def first_occurences(self,nums,X):
        left = 0
        right = len(nums)-1

        result = -1

        while left <= right:
            mid = (left+right)//2

            if nums[mid] == X:
                result = mid
                right = mid-1
            elif nums[mid]<X:
                left = mid+1
            else:
                right = mid-1

        return result
    

    def last_occurences(self,nums,X):
        left = 0
        right = len(nums)-1

        result = -1

        while left <= right:
            mid = (left+right)//2

            if nums[mid] == X:
                result = mid
                left = mid+1

            elif nums[mid]< X:
                left = mid+1
            else:
                right = mid-1

        return result
    

    def Occurence_Finder(self,nums,X):

        first =self.first_occurences(nums,X)

        if first == -1:
            return 0
        
        last = self.last_occurences(nums,X)

        return last-first+1
    

a = OccurenceFinder()
b = a.Occurence_Finder([1,1,1,1,1,1,1,1,1,1,1,2,3,4,5,6,7,8,9,10],1)
print(b)

        
            

