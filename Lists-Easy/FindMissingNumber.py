class MissingNumber:
    def MissingNumberInArray(self,nums):
        n = len(nums)+1
        TotalArrayElementSum = n*(n+1)//2
        ElementsInArraySum = sum(nums)

        return TotalArrayElementSum-ElementsInArraySum
    
a = MissingNumber()
b = a.MissingNumberInArray([1,2,3,4,5,6,7,8,9,10])
print(b)
