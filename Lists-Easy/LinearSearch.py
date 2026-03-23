class LinearSearch:
    def TargetFinder(self,nums,x):
        n = len(nums)

        for i in range(0,n):
            if nums[i] == x:
                return i
        return ''
    
a = LinearSearch()
b = a.TargetFinder([1,5,7,8,96,5,41,5,2,13,5,2,5,6,6,8,5,3,2],7)
print(b)

