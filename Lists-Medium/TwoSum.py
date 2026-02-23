class TwoSum:
    def TwoSumProblem(self,nums,X):
        n = len(nums)-1
        seen = set()


        for i in range(n):
            remain = X - nums[i]

            if remain in seen:
                return f"{nums[i]} and {remain}"
            else:
                seen.add(nums[i])


        return ''
    
a = TwoSum()
b = a.TwoSumProblem([1,2,3,4,85,96,5,2,3,2,4,5,6,3,7,4,1,2,5],7)
print((b))

