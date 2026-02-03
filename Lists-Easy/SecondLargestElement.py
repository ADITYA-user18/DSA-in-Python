class SLarger:
    def SecondLargest(self,nums):
        
        first = -float('inf')
        second = -float('inf')
        

        for num in nums:
            if num > first:
                second = first
                first = num
            elif num > second and num!= first:
                second = num
        return second
    

a = SLarger()
b = a.SecondLargest([1,2,3,4,5,6,78,9])
print(b)
     
                


